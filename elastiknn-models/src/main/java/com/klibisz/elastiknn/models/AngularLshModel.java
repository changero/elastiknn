package com.klibisz.elastiknn.models;

import com.klibisz.elastiknn.storage.BitBuffer;

import static com.klibisz.elastiknn.models.Utils.dot;
import static com.klibisz.elastiknn.models.Utils.magnitude;
import static com.klibisz.elastiknn.storage.UnsafeSerialization.writeInt;

import java.util.Arrays;
import java.util.Random;

public class AngularLshModel implements HashingModel.DenseFloat {

    private final int L;
    private final int k;
    private final float[][] planes;

    /**
     * Locality sensitive hashing model for Angular similarity.
     * Uses the random hyperplanes method described in Mining Massive Datasets chapter 3.
     * @param dims length of the vectors hashed by this model
     * @param L number of hash tables
     * @param k number of hash functions concatenated to form a hash for each table
     * @param rng random number generator used to instantiate model parameters
     */
    public AngularLshModel(int dims, int L, int k, Random rng) {
        this.L = L;
        this.k = k;
        this.planes = new float[L * k][dims];
        for (int i = 0; i < this.planes.length; i++) {
            for (int j = 0; j < dims; j++) {
                this.planes[i][j] = (float) rng.nextGaussian();
            }
        }
    }

    @Override
    public HashAndFreq[] hash(float[] values) {

        // Normalize the vector.
        float[] valuesNormalized = values;
        double magnitude = magnitude(values);
        if (magnitude < 0.99 || magnitude > 1.01) {
            valuesNormalized = Arrays.copyOf(values, values.length);
            for (int i = 0; i < valuesNormalized.length; i++) valuesNormalized[i] /= magnitude;
        }

        HashAndFreq[] hashes = new HashAndFreq[L];
        for (int ixL = 0; ixL < L; ixL++) {
            BitBuffer.IntBuffer buf = new BitBuffer.IntBuffer(writeInt(ixL));
            for (int ixk = 0; ixk < k; ixk++) {
                float dot = dot(planes[ixL * k + ixk], valuesNormalized);
                if (dot > 0) buf.putOne();
                else buf.putZero();
            }
            hashes[ixL] = HashAndFreq.once(buf.toByteArray());
        }
        return hashes;
    }

}
