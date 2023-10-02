# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/reflection_probe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2
from common import bounds_pb2 as common_dot_bounds__pb2
from common import color_pb2 as common_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cunity/reflection_probe.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x13\x63ommon/bounds.proto\x1a\x12\x63ommon/color.proto\"L\n\x15ReflectionProbeCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"d\n\x1cReflectionProbeUpdateEnabled\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xf7\x06\n\x15ReflectionProbeUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x35\n\x04mode\x18\x02 \x01(\x0e\x32\'.plume.sample.unity.ReflectionProbeMode\x12\x44\n\x0crefresh_mode\x18\x03 \x01(\x0e\x32..plume.sample.unity.ReflectionProbeRefreshMode\x12M\n\x11time_slicing_mode\x18\x04 \x01(\x0e\x32\x32.plume.sample.unity.ReflectionProbeTimeSlicingMode\x12\x42\n\x0b\x63lear_flags\x18\x05 \x01(\x0e\x32-.plume.sample.unity.ReflectionProbeClearFlags\x12\x12\n\nimportance\x18\x06 \x01(\x05\x12\x11\n\tintensity\x18\x07 \x01(\x02\x12\x17\n\x0fnear_clip_plane\x18\x08 \x01(\x02\x12\x16\n\x0e\x66\x61r_clip_plane\x18\t \x01(\x02\x12\x1e\n\x16render_dynamic_objects\x18\n \x01(\x08\x12\x16\n\x0e\x62ox_projection\x18\x0b \x01(\x08\x12\x16\n\x0e\x62lend_distance\x18\x0c \x01(\x02\x12+\n\x06\x62ounds\x18\r \x01(\x0b\x32\x1b.plume.sample.common.Bounds\x12\x12\n\nresolution\x18\x0e \x01(\x05\x12\x0b\n\x03hdr\x18\x0f \x01(\x08\x12\x17\n\x0fshadow_distance\x18\x10 \x01(\x02\x12\x34\n\x10\x62\x61\x63kground_color\x18\x11 \x01(\x0b\x32\x1a.plume.sample.common.Color\x12\x14\n\x0c\x63ulling_mask\x18\x12 \x01(\x05\x12I\n\x17\x63ustom_baked_texture_id\x18\x13 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x00\x88\x01\x01\x12\x42\n\x10\x62\x61ked_texture_id\x18\x14 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01\x88\x01\x01\x42\x1a\n\x18_custom_baked_texture_idB\x13\n\x11_baked_texture_id*|\n\x13ReflectionProbeMode\x12\x1f\n\x1bREFLECTION_PROBE_MODE_BAKED\x10\x00\x12 \n\x1cREFLECTION_PROBE_MODE_CUSTOM\x10\x01\x12\"\n\x1eREFLECTION_PROBE_MODE_REALTIME\x10\x02*r\n\x19ReflectionProbeClearFlags\x12\'\n#REFLECTION_PROBE_CLEAR_FLAGS_SKYBOX\x10\x00\x12,\n(REFLECTION_PROBE_CLEAR_FLAGS_SOLID_COLOR\x10\x01*\xa8\x01\n\x1aReflectionProbeRefreshMode\x12*\n&REFLECTION_PROBE_REFRESH_MODE_ON_AWAKE\x10\x00\x12-\n)REFLECTION_PROBE_REFRESH_MODE_EVERY_FRAME\x10\x01\x12/\n+REFLECTION_PROBE_REFRESH_MODE_VIA_SCRIPTING\x10\x02*\xcb\x01\n\x1eReflectionProbeTimeSlicingMode\x12\x38\n4REFLECTION_PROBE_TIME_SLICING_MODE_ALL_FACES_AT_ONCE\x10\x00\x12\x37\n3REFLECTION_PROBE_TIME_SLICING_MODE_INDIVIDUAL_FACES\x10\x01\x12\x36\n2REFLECTION_PROBE_TIME_SLICING_MODE_NO_TIME_SLICING\x10\x02\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.reflection_probe_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_REFLECTIONPROBEMODE']._serialized_start=1188
  _globals['_REFLECTIONPROBEMODE']._serialized_end=1312
  _globals['_REFLECTIONPROBECLEARFLAGS']._serialized_start=1314
  _globals['_REFLECTIONPROBECLEARFLAGS']._serialized_end=1428
  _globals['_REFLECTIONPROBEREFRESHMODE']._serialized_start=1431
  _globals['_REFLECTIONPROBEREFRESHMODE']._serialized_end=1599
  _globals['_REFLECTIONPROBETIMESLICINGMODE']._serialized_start=1602
  _globals['_REFLECTIONPROBETIMESLICINGMODE']._serialized_end=1805
  _globals['_REFLECTIONPROBECREATE']._serialized_start=118
  _globals['_REFLECTIONPROBECREATE']._serialized_end=194
  _globals['_REFLECTIONPROBEUPDATEENABLED']._serialized_start=196
  _globals['_REFLECTIONPROBEUPDATEENABLED']._serialized_end=296
  _globals['_REFLECTIONPROBEUPDATE']._serialized_start=299
  _globals['_REFLECTIONPROBEUPDATE']._serialized_end=1186
# @@protoc_insertion_point(module_scope)
