# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scalapb/scalapb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scalapb/scalapb.proto',
  package='scalapb',
  syntax='proto2',
  serialized_options=_b('\n\017scalapb.options\342?\023\n\017scalapb.options\020\001'),
  serialized_pb=_b('\n\x15scalapb/scalapb.proto\x12\x07scalapb\x1a google/protobuf/descriptor.proto\"\xed\x04\n\x0eScalaPbOptions\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66lat_package\x18\x02 \x01(\x08\x12\x0e\n\x06import\x18\x03 \x03(\t\x12\x10\n\x08preamble\x18\x04 \x03(\t\x12\x13\n\x0bsingle_file\x18\x05 \x01(\x08\x12\x1d\n\x15no_primitive_wrappers\x18\x07 \x01(\x08\x12\x1a\n\x12primitive_wrappers\x18\x06 \x01(\x08\x12\x17\n\x0f\x63ollection_type\x18\x08 \x01(\t\x12\x1f\n\x17preserve_unknown_fields\x18\t \x01(\x08\x12\x13\n\x0bobject_name\x18\n \x01(\t\x12\x33\n\x05scope\x18\x0b \x01(\x0e\x32$.scalapb.ScalaPbOptions.OptionsScope\x12\x14\n\x06lenses\x18\x0c \x01(\x08:\x04true\x12\x1f\n\x17retain_source_code_info\x18\r \x01(\x08\x12\x10\n\x08map_type\x18\x0e \x01(\t\x12(\n no_default_values_in_constructor\x18\x0f \x01(\x08\x12\x42\n\x11\x65num_value_naming\x18\x10 \x01(\x0e\x32\'.scalapb.ScalaPbOptions.EnumValueNaming\x12\'\n\x1dtest_only_no_java_conversions\x18\xa1\x8d\x06 \x01(\x08\"%\n\x0cOptionsScope\x12\x08\n\x04\x46ILE\x10\x00\x12\x0b\n\x07PACKAGE\x10\x01\"2\n\x0f\x45numValueNaming\x12\x0f\n\x0b\x41S_IN_PROTO\x10\x00\x12\x0e\n\nCAMEL_CASE\x10\x01\"\xac\x01\n\x0eMessageOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\x12\x19\n\x11\x63ompanion_extends\x18\x02 \x03(\t\x12\x13\n\x0b\x61nnotations\x18\x03 \x03(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1d\n\x15\x63ompanion_annotations\x18\x05 \x03(\t\x12\x1c\n\x14sealed_oneof_extends\x18\x06 \x03(\t\x12\x0e\n\x06no_box\x18\x07 \x01(\x08\"\xa6\x01\n\x0c\x46ieldOptions\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\nscala_name\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_type\x18\x03 \x01(\t\x12\x10\n\x08key_type\x18\x04 \x01(\t\x12\x12\n\nvalue_type\x18\x05 \x01(\t\x12\x13\n\x0b\x61nnotations\x18\x06 \x03(\t\x12\x10\n\x08map_type\x18\x07 \x01(\t\x12\x0e\n\x06no_box\x18\x1e \x01(\x08\"G\n\x0b\x45numOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\x12\x19\n\x11\x63ompanion_extends\x18\x02 \x03(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"7\n\x10\x45numValueOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\x12\x12\n\nscala_name\x18\x02 \x01(\t\"\x1f\n\x0cOneofOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t:G\n\x07options\x12\x1c.google.protobuf.FileOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.ScalaPbOptions:J\n\x07message\x12\x1f.google.protobuf.MessageOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.MessageOptions:D\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.FieldOptions:I\n\x0c\x65num_options\x12\x1c.google.protobuf.EnumOptions\x18\xfc\x07 \x01(\x0b\x32\x14.scalapb.EnumOptions:Q\n\nenum_value\x12!.google.protobuf.EnumValueOptions\x18\xfc\x07 \x01(\x0b\x32\x19.scalapb.EnumValueOptions:D\n\x05oneof\x12\x1d.google.protobuf.OneofOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.OneofOptionsB\'\n\x0fscalapb.options\xe2?\x13\n\x0fscalapb.options\x10\x01')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


OPTIONS_FIELD_NUMBER = 1020
options = _descriptor.FieldDescriptor(
  name='options', full_name='scalapb.options', index=0,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MESSAGE_FIELD_NUMBER = 1020
message = _descriptor.FieldDescriptor(
  name='message', full_name='scalapb.message', index=1,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FIELD_FIELD_NUMBER = 1020
field = _descriptor.FieldDescriptor(
  name='field', full_name='scalapb.field', index=2,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_OPTIONS_FIELD_NUMBER = 1020
enum_options = _descriptor.FieldDescriptor(
  name='enum_options', full_name='scalapb.enum_options', index=3,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_VALUE_FIELD_NUMBER = 1020
enum_value = _descriptor.FieldDescriptor(
  name='enum_value', full_name='scalapb.enum_value', index=4,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ONEOF_FIELD_NUMBER = 1020
oneof = _descriptor.FieldDescriptor(
  name='oneof', full_name='scalapb.oneof', index=5,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

_SCALAPBOPTIONS_OPTIONSSCOPE = _descriptor.EnumDescriptor(
  name='OptionsScope',
  full_name='scalapb.ScalaPbOptions.OptionsScope',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=601,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_SCALAPBOPTIONS_OPTIONSSCOPE)

_SCALAPBOPTIONS_ENUMVALUENAMING = _descriptor.EnumDescriptor(
  name='EnumValueNaming',
  full_name='scalapb.ScalaPbOptions.EnumValueNaming',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AS_IN_PROTO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMEL_CASE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=640,
  serialized_end=690,
)
_sym_db.RegisterEnumDescriptor(_SCALAPBOPTIONS_ENUMVALUENAMING)


_SCALAPBOPTIONS = _descriptor.Descriptor(
  name='ScalaPbOptions',
  full_name='scalapb.ScalaPbOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='scalapb.ScalaPbOptions.package_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flat_package', full_name='scalapb.ScalaPbOptions.flat_package', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='import', full_name='scalapb.ScalaPbOptions.import', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preamble', full_name='scalapb.ScalaPbOptions.preamble', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_file', full_name='scalapb.ScalaPbOptions.single_file', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_primitive_wrappers', full_name='scalapb.ScalaPbOptions.no_primitive_wrappers', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primitive_wrappers', full_name='scalapb.ScalaPbOptions.primitive_wrappers', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_type', full_name='scalapb.ScalaPbOptions.collection_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preserve_unknown_fields', full_name='scalapb.ScalaPbOptions.preserve_unknown_fields', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='scalapb.ScalaPbOptions.object_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='scalapb.ScalaPbOptions.scope', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lenses', full_name='scalapb.ScalaPbOptions.lenses', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retain_source_code_info', full_name='scalapb.ScalaPbOptions.retain_source_code_info', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_type', full_name='scalapb.ScalaPbOptions.map_type', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_default_values_in_constructor', full_name='scalapb.ScalaPbOptions.no_default_values_in_constructor', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_value_naming', full_name='scalapb.ScalaPbOptions.enum_value_naming', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_only_no_java_conversions', full_name='scalapb.ScalaPbOptions.test_only_no_java_conversions', index=16,
      number=100001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCALAPBOPTIONS_OPTIONSSCOPE,
    _SCALAPBOPTIONS_ENUMVALUENAMING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=690,
)


_MESSAGEOPTIONS = _descriptor.Descriptor(
  name='MessageOptions',
  full_name='scalapb.MessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extends', full_name='scalapb.MessageOptions.extends', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companion_extends', full_name='scalapb.MessageOptions.companion_extends', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='scalapb.MessageOptions.annotations', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='scalapb.MessageOptions.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companion_annotations', full_name='scalapb.MessageOptions.companion_annotations', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sealed_oneof_extends', full_name='scalapb.MessageOptions.sealed_oneof_extends', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_box', full_name='scalapb.MessageOptions.no_box', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=865,
)


_FIELDOPTIONS = _descriptor.Descriptor(
  name='FieldOptions',
  full_name='scalapb.FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='scalapb.FieldOptions.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scala_name', full_name='scalapb.FieldOptions.scala_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_type', full_name='scalapb.FieldOptions.collection_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_type', full_name='scalapb.FieldOptions.key_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='scalapb.FieldOptions.value_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='scalapb.FieldOptions.annotations', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_type', full_name='scalapb.FieldOptions.map_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_box', full_name='scalapb.FieldOptions.no_box', index=7,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=868,
  serialized_end=1034,
)


_ENUMOPTIONS = _descriptor.Descriptor(
  name='EnumOptions',
  full_name='scalapb.EnumOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extends', full_name='scalapb.EnumOptions.extends', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companion_extends', full_name='scalapb.EnumOptions.companion_extends', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='scalapb.EnumOptions.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1036,
  serialized_end=1107,
)


_ENUMVALUEOPTIONS = _descriptor.Descriptor(
  name='EnumValueOptions',
  full_name='scalapb.EnumValueOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extends', full_name='scalapb.EnumValueOptions.extends', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scala_name', full_name='scalapb.EnumValueOptions.scala_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1109,
  serialized_end=1164,
)


_ONEOFOPTIONS = _descriptor.Descriptor(
  name='OneofOptions',
  full_name='scalapb.OneofOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extends', full_name='scalapb.OneofOptions.extends', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1166,
  serialized_end=1197,
)

_SCALAPBOPTIONS.fields_by_name['scope'].enum_type = _SCALAPBOPTIONS_OPTIONSSCOPE
_SCALAPBOPTIONS.fields_by_name['enum_value_naming'].enum_type = _SCALAPBOPTIONS_ENUMVALUENAMING
_SCALAPBOPTIONS_OPTIONSSCOPE.containing_type = _SCALAPBOPTIONS
_SCALAPBOPTIONS_ENUMVALUENAMING.containing_type = _SCALAPBOPTIONS
DESCRIPTOR.message_types_by_name['ScalaPbOptions'] = _SCALAPBOPTIONS
DESCRIPTOR.message_types_by_name['MessageOptions'] = _MESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['FieldOptions'] = _FIELDOPTIONS
DESCRIPTOR.message_types_by_name['EnumOptions'] = _ENUMOPTIONS
DESCRIPTOR.message_types_by_name['EnumValueOptions'] = _ENUMVALUEOPTIONS
DESCRIPTOR.message_types_by_name['OneofOptions'] = _ONEOFOPTIONS
DESCRIPTOR.extensions_by_name['options'] = options
DESCRIPTOR.extensions_by_name['message'] = message
DESCRIPTOR.extensions_by_name['field'] = field
DESCRIPTOR.extensions_by_name['enum_options'] = enum_options
DESCRIPTOR.extensions_by_name['enum_value'] = enum_value
DESCRIPTOR.extensions_by_name['oneof'] = oneof
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScalaPbOptions = _reflection.GeneratedProtocolMessageType('ScalaPbOptions', (_message.Message,), {
  'DESCRIPTOR' : _SCALAPBOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.ScalaPbOptions)
  })
_sym_db.RegisterMessage(ScalaPbOptions)

MessageOptions = _reflection.GeneratedProtocolMessageType('MessageOptions', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.MessageOptions)
  })
_sym_db.RegisterMessage(MessageOptions)

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), {
  'DESCRIPTOR' : _FIELDOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.FieldOptions)
  })
_sym_db.RegisterMessage(FieldOptions)

EnumOptions = _reflection.GeneratedProtocolMessageType('EnumOptions', (_message.Message,), {
  'DESCRIPTOR' : _ENUMOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.EnumOptions)
  })
_sym_db.RegisterMessage(EnumOptions)

EnumValueOptions = _reflection.GeneratedProtocolMessageType('EnumValueOptions', (_message.Message,), {
  'DESCRIPTOR' : _ENUMVALUEOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.EnumValueOptions)
  })
_sym_db.RegisterMessage(EnumValueOptions)

OneofOptions = _reflection.GeneratedProtocolMessageType('OneofOptions', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFOPTIONS,
  '__module__' : 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.OneofOptions)
  })
_sym_db.RegisterMessage(OneofOptions)

options.message_type = _SCALAPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(options)
message.message_type = _MESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message)
field.message_type = _FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)
enum_options.message_type = _ENUMOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_options)
enum_value.message_type = _ENUMVALUEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value)
oneof.message_type = _ONEOFOPTIONS
google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
