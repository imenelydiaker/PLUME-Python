# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lsl/stream_sample.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lsl import stream_info_pb2 as lsl_dot_stream__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17lsl/stream_sample.proto\x12\x10plume.sample.lsl\x1a\x15lsl/stream_info.proto\"\xd6\x03\n\x0cStreamSample\x12\x31\n\x0bstream_info\x18\x01 \x01(\x0b\x32\x1c.plume.sample.lsl.StreamInfo\x12\x36\n\x0b\x66loat_value\x18\x05 \x01(\x0b\x32\x1f.plume.sample.lsl.RepeatedFloatH\x00\x12\x38\n\x0c\x64ouble_value\x18\x06 \x01(\x0b\x32 .plume.sample.lsl.RepeatedDoubleH\x00\x12\x38\n\x0cstring_value\x18\x07 \x01(\x0b\x32 .plume.sample.lsl.RepeatedStringH\x00\x12\x35\n\nint8_value\x18\x08 \x01(\x0b\x32\x1f.plume.sample.lsl.RepeatedInt32H\x00\x12\x36\n\x0bint16_value\x18\t \x01(\x0b\x32\x1f.plume.sample.lsl.RepeatedInt32H\x00\x12\x36\n\x0bint32_value\x18\n \x01(\x0b\x32\x1f.plume.sample.lsl.RepeatedInt32H\x00\x12\x36\n\x0bint64_value\x18\x0b \x01(\x0b\x32\x1f.plume.sample.lsl.RepeatedInt64H\x00\x42\x08\n\x06values\"\x1e\n\rRepeatedFloat\x12\r\n\x05value\x18\x01 \x03(\x02\"\x1f\n\x0eRepeatedDouble\x12\r\n\x05value\x18\x01 \x03(\x01\"\x1f\n\x0eRepeatedString\x12\r\n\x05value\x18\x01 \x03(\t\"\x1e\n\rRepeatedInt32\x12\r\n\x05value\x18\x01 \x03(\x05\"\x1e\n\rRepeatedInt64\x12\r\n\x05value\x18\x01 \x03(\x03\x42\x13\xaa\x02\x10PLUME.Sample.LSLb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lsl.stream_sample_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\020PLUME.Sample.LSL'
  _globals['_STREAMSAMPLE']._serialized_start=69
  _globals['_STREAMSAMPLE']._serialized_end=539
  _globals['_REPEATEDFLOAT']._serialized_start=541
  _globals['_REPEATEDFLOAT']._serialized_end=571
  _globals['_REPEATEDDOUBLE']._serialized_start=573
  _globals['_REPEATEDDOUBLE']._serialized_end=604
  _globals['_REPEATEDSTRING']._serialized_start=606
  _globals['_REPEATEDSTRING']._serialized_end=637
  _globals['_REPEATEDINT32']._serialized_start=639
  _globals['_REPEATEDINT32']._serialized_end=669
  _globals['_REPEATEDINT64']._serialized_start=671
  _globals['_REPEATEDINT64']._serialized_end=701
# @@protoc_insertion_point(module_scope)
