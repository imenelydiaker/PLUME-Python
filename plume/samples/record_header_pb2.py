# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: record_header.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import record_version_pb2 as record__version__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13record_header.proto\x12\x0cplume.sample\x1a\x14record_version.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x01\n\x0cRecordHeader\x12\x37\n\x10recorder_version\x18\x01 \x01(\x0b\x32\x1d.plume.sample.RecorderVersion\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nidentifier\x18\x03 \x01(\t\x12\x16\n\x0e\x65xtra_metadata\x18\x04 \x01(\tB\x0f\xaa\x02\x0cPLUME.Sampleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'record_header_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\014PLUME.Sample'
  _globals['_RECORDHEADER']._serialized_start=93
  _globals['_RECORDHEADER']._serialized_end=256
# @@protoc_insertion_point(module_scope)