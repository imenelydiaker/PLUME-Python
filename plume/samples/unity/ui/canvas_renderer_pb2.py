# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/canvas_renderer.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eunity/ui/canvas_renderer.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"K\n\x14\x43\x61nvasRendererCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"L\n\x15\x43\x61nvasRendererDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"\x89\x01\n\x14\x43\x61nvasRendererUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\"\n\x15\x63ull_transparent_mesh\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\x18\n\x16_cull_transparent_meshB\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.ui.canvas_renderer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025PLUME.Sample.Unity.UI'
  _globals['_CANVASRENDERERCREATE']._serialized_start=79
  _globals['_CANVASRENDERERCREATE']._serialized_end=154
  _globals['_CANVASRENDERERDESTROY']._serialized_start=156
  _globals['_CANVASRENDERERDESTROY']._serialized_end=232
  _globals['_CANVASRENDERERUPDATE']._serialized_start=235
  _globals['_CANVASRENDERERUPDATE']._serialized_end=372
# @@protoc_insertion_point(module_scope)
