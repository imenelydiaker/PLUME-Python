# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/rect_transform.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x1dunity/ui/rect_transform.proto\x12\x12plume.sample.unity\x1a\x14\x63ommon/vector2.proto\x1a\x17unity/identifiers.proto\"J\n\x13RectTransformCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"K\n\x14RectTransformDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"\xac\x03\n\x13RectTransformUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\x12\x35\n\nanchor_min\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x00\x88\x01\x01\x12\x35\n\nanchor_max\x18\x03 \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x01\x88\x01\x01\x12<\n\x11\x61nchored_position\x18\x04 \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x02\x88\x01\x01\x12\x35\n\nsize_delta\x18\x05 \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x03\x88\x01\x01\x12\x30\n\x05pivot\x18\x06 \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x04\x88\x01\x01\x42\r\n\x0b_anchor_minB\r\n\x0b_anchor_maxB\x14\n\x12_anchored_positionB\r\n\x0b_size_deltaB\x08\n\x06_pivotB\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "unity.ui.rect_transform_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\025PLUME.Sample.Unity.UI"
    _globals["_RECTTRANSFORMCREATE"]._serialized_start = 100
    _globals["_RECTTRANSFORMCREATE"]._serialized_end = 174
    _globals["_RECTTRANSFORMDESTROY"]._serialized_start = 176
    _globals["_RECTTRANSFORMDESTROY"]._serialized_end = 251
    _globals["_RECTTRANSFORMUPDATE"]._serialized_start = 254
    _globals["_RECTTRANSFORMUPDATE"]._serialized_end = 682
# @@protoc_insertion_point(module_scope)
