# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/render_settings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import color_pb2 as common_dot_color__pb2
from common import spherical_harmonics_l2_pb2 as common_dot_spherical__harmonics__l2__pb2
from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bunity/render_settings.proto\x12\x12plume.sample.unity\x1a\x12\x63ommon/color.proto\x1a#common/spherical_harmonics_l2.proto\x1a\x17unity/identifiers.proto\"\xe8\x08\n\x14RenderSettingsUpdate\x12\x39\n\x15\x61mbient_equator_color\x18\x01 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x38\n\x14\x61mbient_ground_color\x18\x02 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x19\n\x11\x61mbient_intensity\x18\x03 \x01(\x02\x12\x31\n\rambient_light\x18\x04 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x35\n\x0c\x61mbient_mode\x18\x05 \x01(\x0e\x32\x1f.plume.sample.unity.AmbientMode\x12@\n\rambient_probe\x18\x06 \x01(\x0b\x32).plume.sample.common.SphericalHarmonicsL2\x12\x35\n\x11\x61mbient_sky_color\x18\x07 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x46\n\x14\x63ustom_reflection_id\x18\x08 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x00\x88\x01\x01\x12J\n\x17\x64\x65\x66\x61ult_reflection_mode\x18\t \x01(\x0e\x32).plume.sample.unity.DefaultReflectionMode\x12%\n\x1d\x64\x65\x66\x61ult_reflection_resolution\x18\n \x01(\x05\x12\x18\n\x10\x66lare_fade_speed\x18\x0b \x01(\x02\x12\x16\n\x0e\x66lare_strength\x18\x0c \x01(\x02\x12\x0b\n\x03\x66og\x18\r \x01(\x08\x12-\n\tfog_color\x18\x0e \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x13\n\x0b\x66og_density\x18\x0f \x01(\x02\x12\x18\n\x10\x66og_end_distance\x18\x10 \x01(\x02\x12-\n\x08\x66og_mode\x18\x11 \x01(\x0e\x32\x1b.plume.sample.unity.FogMode\x12\x1a\n\x12\x66og_start_distance\x18\x12 \x01(\x02\x12\x15\n\rhalo_strength\x18\x13 \x01(\x02\x12\x1a\n\x12reflection_bounces\x18\x14 \x01(\x05\x12\x1c\n\x14reflection_intensity\x18\x15 \x01(\x02\x12;\n\tskybox_id\x18\x16 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01\x88\x01\x01\x12<\n\x18subtractive_shadow_color\x18\x17 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12<\n\x06sun_id\x18\x18 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierH\x02\x88\x01\x01\x42\x17\n\x15_custom_reflection_idB\x0c\n\n_skybox_idB\t\n\x07_sun_id*q\n\x0b\x41mbientMode\x12\x17\n\x13\x41MBIENT_MODE_SKYBOX\x10\x00\x12\x19\n\x15\x41MBIENT_MODE_TRILIGHT\x10\x01\x12\x15\n\x11\x41MBIENT_MODE_FLAT\x10\x02\x12\x17\n\x13\x41MBIENT_MODE_CUSTOM\x10\x03*_\n\x15\x44\x65\x66\x61ultReflectionMode\x12\"\n\x1e\x44\x45\x46\x41ULT_REFLECTION_MODE_SKYBOX\x10\x00\x12\"\n\x1e\x44\x45\x46\x41ULT_REFLECTION_MODE_CUSTOM\x10\x01*Z\n\x07\x46ogMode\x12\x13\n\x0f\x46OG_MODE_LINEAR\x10\x00\x12\x18\n\x14\x46OG_MODE_EXPONENTIAL\x10\x01\x12 \n\x1c\x46OG_MODE_EXPONENTIAL_SQUARED\x10\x02\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.render_settings_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_AMBIENTMODE']._serialized_start=1264
  _globals['_AMBIENTMODE']._serialized_end=1377
  _globals['_DEFAULTREFLECTIONMODE']._serialized_start=1379
  _globals['_DEFAULTREFLECTIONMODE']._serialized_end=1474
  _globals['_FOGMODE']._serialized_start=1476
  _globals['_FOGMODE']._serialized_end=1566
  _globals['_RENDERSETTINGSUPDATE']._serialized_start=134
  _globals['_RENDERSETTINGSUPDATE']._serialized_end=1262
# @@protoc_insertion_point(module_scope)
