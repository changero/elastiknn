package org.apache.lucene.search;

import com.klibisz.elastiknn.search.ArrayHitCounter;
import com.klibisz.elastiknn.search.HitCounter;
import com.klibisz.elastiknn.models.HashAndFreq;
import com.klibisz.elastiknn.utils.Pair;
import org.apache.lucene.index.*;
import org.apache.lucene.util.BytesRef;

import java.io.IOException;
import java.util.*;
import java.util.function.Function;

/**
 * Query that finds docs containing the given hashes hashes (Lucene terms), and then applies a scoring function to the
 * docs containing the most matching hashes. Largely based on Lucene's TermsInSetQuery.
 */
public class MatchHashesAndScoreQuery extends Query {

    public interface ScoreFunction {
        double score(int docId, int numMatchingHashes);
    }

    private final String field;
    private final HashAndFreq[] hashAndFrequencies;
    private final int candidates;
    private final IndexReader indexReader;
    private final Function<LeafReaderContext, ScoreFunction> scoreFunctionBuilder;

    public MatchHashesAndScoreQuery(final String field,
                                    final HashAndFreq[] hashAndFrequencies,
                                    final int candidates,
                                    final IndexReader indexReader,
                                    final Function<LeafReaderContext, ScoreFunction> scoreFunctionBuilder) {
        // `countMatches` expects hashes to be in sorted order.
        // java's sort seems to be faster than lucene's ArrayUtil.
        Arrays.sort(hashAndFrequencies, HashAndFreq::compareTo);

        this.field = field;
        this.hashAndFrequencies = hashAndFrequencies;
        this.candidates = candidates;
        this.indexReader = indexReader;
        this.scoreFunctionBuilder = scoreFunctionBuilder;
    }

    @Override
    public Weight createWeight(IndexSearcher searcher, ScoreMode scoreMode, float boost) {

        return new Weight(this) {

            /**
             * Builds and returns a Pair containing:
             * - Integer[] array of the top `candidates` doc IDs.
             * - int[] array where the indices are doc IDs and values are the score for each doc ID.
             */
            private Pair<Integer[], int[]> countHits(LeafReader reader) throws IOException {
                Terms terms = reader.terms(field);
                // terms seem to be null after deleting docs. https://github.com/alexklibisz/elastiknn/issues/158
                if (terms == null) return new Pair<>(new Integer[0], new int[0]);
                else {

                    // TODO: Where is the right place to use the live docs bitset to check for deleted docs?
                    // Bits liveDocs = reader.getLiveDocs();

                    TermsEnum termsEnum = terms.iterator();

                    // Array of PostingsEnums, one for each term.
                    final PostingsEnum[] postingsEnums = new PostingsEnum[hashAndFrequencies.length];

                    // Total number of docs matching the query terms. Used as a stopping criteria.
                    int totalDocs = 0;

                    // Populate postingsEnums and totalDocs.
                    for (int i = 0; i < hashAndFrequencies.length; i++) {
                        if (termsEnum.seekExact(new BytesRef(hashAndFrequencies[i].getHash()))) {
                            PostingsEnum postingsEnum = null;
                            postingsEnums[i] = termsEnum.postings(postingsEnum, PostingsEnum.FREQS);
                            totalDocs += termsEnum.docFreq();
                        }
                    }

                    // Number of query terms matched in each doc.
                    int[] scores = new int[reader.maxDoc()];

                    // Doc id of the last doc seen by each postings enum.
                    int[] currentScores = new int[postingsEnums.length];

                    // Track the top k doc IDs. Note using counter for comparator.
                    PriorityQueue<Integer> minHeap = new PriorityQueue<>(candidates, Comparator.comparingInt(i -> scores[i]));

                    // Track the min doc id on each pass through the postings enums.
                    int minDocId = Integer.MAX_VALUE;

                    int docsVisited = 0;

                    while (true) {
                        // Need to remember the previous min doc id.
                        int prevMinDocID = minDocId;
                        minDocId = Integer.MAX_VALUE;

                        // Iterate the postings and update the various state trackers.
                        for (int i = 0; i < postingsEnums.length; i++) {
                            if (postingsEnums[i] != null) {
                                PostingsEnum docs = postingsEnums[i];
                                if (docs.docID() != DocIdSetIterator.NO_MORE_DOCS && docs.nextDoc() != DocIdSetIterator.NO_MORE_DOCS) {
                                    docsVisited++;
                                    minDocId = Math.min(minDocId, docs.docID());
                                    int score = Math.min(hashAndFrequencies[i].getFreq(), docs.freq());
                                    scores[docs.docID()] += score;
                                    currentScores[i] = score;
                                }
                            }
                        }

                        // Set the threshold as the sum of the last score for each term.
                        int threshold = 0;
                        for (int score : currentScores) threshold += score;

//                        if (minHeap.size() > 0) {
//                            System.out.printf("Threshold = [%d], kth greatest score = [%d]\n", threshold, scores[minHeap.peek()]);
//                        }

                        // Any doc id between the previous min and the current min can be added to the heap.
                        for (int docID = prevMinDocID; docID < minDocId; docID++) {
                            if (minHeap.size() < candidates) minHeap.add(docID);
                            else if (scores[docID] > scores[minHeap.peek()]) {
                                minHeap.remove();
                                minHeap.add(docID);
                            }
                        }

                        // Regular stopping condition.
                        if (docsVisited == totalDocs) break;

                        // Early stopping condition.
                        if (minHeap.size() == candidates && scores[minHeap.peek()] >= threshold) {
                            System.out.printf("Stopping %d, %d, %d, %d, %d\n", docsVisited, totalDocs, minDocId, scores[minHeap.peek()], threshold);
                            break;
                        }
                    }

                    return new Pair<>(minHeap.toArray(new Integer[0]), scores);
                }
            }

            private DocIdSetIterator buildDocIdSetIterator(Integer[] topDocIDs) {
                if (topDocIDs.length == 0) return DocIdSetIterator.empty();
                else {

                    // Lucene likes doc IDs in sorted order.
                    Arrays.sort(topDocIDs);

                    // Return an iterator over the doc ids >= the min candidate count.
                    return new DocIdSetIterator() {

                        private int i = -1;
                        private int docID = topDocIDs[0];

                        @Override
                        public int docID() {
                            return docID;
                        }

                        @Override
                        public int nextDoc() {
                            if (i + 1 == topDocIDs.length) {
                                docID = DocIdSetIterator.NO_MORE_DOCS;
                                return docID;
                            } else {
                                docID = topDocIDs[++i];
                                return docID;
                            }
                        }

                        @Override
                        public int advance(int target) {
                            while (docID < target) nextDoc();
                            return docID;
                        }

                        @Override
                        public long cost() {
                            return topDocIDs.length;
                        }
                    };
                }
            }

            @Override
            public void extractTerms(Set<Term> terms) { }

            @Override
            public Explanation explain(LeafReaderContext context, int doc) {
                return Explanation.match( 0, "If someone knows what this should return, please submit a PR. :)");
            }

            @Override
            public Scorer scorer(LeafReaderContext context) throws IOException {
                ScoreFunction scoreFunction = scoreFunctionBuilder.apply(context);
                LeafReader reader = context.reader();
                Pair<Integer[], int[]> countResult = countHits(reader);
                Integer[] topDocIDs = countResult.a;
                int[] scores = countResult.b;
                DocIdSetIterator disi = buildDocIdSetIterator(topDocIDs);

                return new Scorer(this) {
                    @Override
                    public DocIdSetIterator iterator() {
                        return disi;
                    }

                    @Override
                    public float getMaxScore(int upTo) {
                        return Float.MAX_VALUE;
                    }

                    @Override
                    public float score() {
                        return (float) scoreFunction.score(docID(), scores[docID()]);
                    }

                    @Override
                    public int docID() {
                        return disi.docID();
                    }
                };
            }

            @Override
            public boolean isCacheable(LeafReaderContext ctx) {
                return false;
            }
        };
    }

    @Override
    public String toString(String field) {
        return String.format(
                "%s for field [%s] with [%d] hashes and [%d] candidates",
                this.getClass().getSimpleName(),
                this.field,
                this.hashAndFrequencies.length,
                this.candidates);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof MatchHashesAndScoreQuery) {
            MatchHashesAndScoreQuery q = (MatchHashesAndScoreQuery) obj;
            return q.hashCode() == this.hashCode();
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(field, hashAndFrequencies, candidates, indexReader, scoreFunctionBuilder);
    }
}
