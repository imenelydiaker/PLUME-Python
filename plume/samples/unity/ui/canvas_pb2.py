# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/canvas.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15unity/ui/canvas.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"C\n\x0c\x43\x61nvasCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"b\n\x16\x43\x61nvasUpdateRenderMode\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x13\n\x0brender_mode\x18\x02 \x01(\x05\x42\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.ui.canvas_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\025PLUME.Sample.Unity.UI'
  _globals['_CANVASCREATE']._serialized_start=70
  _globals['_CANVASCREATE']._serialized_end=137
  _globals['_CANVASUPDATERENDERMODE']._serialized_start=139
  _globals['_CANVASUPDATERENDERMODE']._serialized_end=237
# @@protoc_insertion_point(module_scope)
