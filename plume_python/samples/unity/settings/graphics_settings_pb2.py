# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/settings/graphics_settings.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&unity/settings/graphics_settings.proto\x12\x1bplume.sample.unity.settings\x1a\x17unity/identifiers.proto\x1a\x12\x63ommon/color.proto"\x97\x01\n\x10GraphicsSettings\x12M\n default_render_pipeline_asset_id\x18\x01 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifier\x12\x34\n\x0b\x63olor_space\x18\x02 \x01(\x0e\x32\x1f.plume.sample.common.ColorSpaceB\x1e\xaa\x02\x1bPLUME.Sample.Unity.Settingsb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "unity.settings.graphics_settings_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\033PLUME.Sample.Unity.Settings"
    _globals["_GRAPHICSSETTINGS"]._serialized_start = 117
    _globals["_GRAPHICSSETTINGS"]._serialized_end = 268
# @@protoc_insertion_point(module_scope)
