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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x1cunity/reflection_probe.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x13\x63ommon/bounds.proto\x1a\x12\x63ommon/color.proto\"L\n\x15ReflectionProbeCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"M\n\x16ReflectionProbeDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"\x8f\n\n\x15ReflectionProbeUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\x12\x14\n\x07\x65nabled\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12:\n\x04mode\x18\x03 \x01(\x0e\x32'.plume.sample.unity.ReflectionProbeModeH\x01\x88\x01\x01\x12I\n\x0crefresh_mode\x18\x04 \x01(\x0e\x32..plume.sample.unity.ReflectionProbeRefreshModeH\x02\x88\x01\x01\x12R\n\x11time_slicing_mode\x18\x05 \x01(\x0e\x32\x32.plume.sample.unity.ReflectionProbeTimeSlicingModeH\x03\x88\x01\x01\x12G\n\x0b\x63lear_flags\x18\x06 \x01(\x0e\x32-.plume.sample.unity.ReflectionProbeClearFlagsH\x04\x88\x01\x01\x12\x17\n\nimportance\x18\x07 \x01(\x05H\x05\x88\x01\x01\x12\x16\n\tintensity\x18\x08 \x01(\x02H\x06\x88\x01\x01\x12\x1c\n\x0fnear_clip_plane\x18\t \x01(\x02H\x07\x88\x01\x01\x12\x1b\n\x0e\x66\x61r_clip_plane\x18\n \x01(\x02H\x08\x88\x01\x01\x12#\n\x16render_dynamic_objects\x18\x0b \x01(\x08H\t\x88\x01\x01\x12\x1b\n\x0e\x62ox_projection\x18\x0c \x01(\x08H\n\x88\x01\x01\x12\x1b\n\x0e\x62lend_distance\x18\r \x01(\x02H\x0b\x88\x01\x01\x12\x30\n\x06\x62ounds\x18\x0e \x01(\x0b\x32\x1b.plume.sample.common.BoundsH\x0c\x88\x01\x01\x12\x17\n\nresolution\x18\x0f \x01(\x05H\r\x88\x01\x01\x12\x10\n\x03hdr\x18\x10 \x01(\x08H\x0e\x88\x01\x01\x12\x1c\n\x0fshadow_distance\x18\x11 \x01(\x02H\x0f\x88\x01\x01\x12\x39\n\x10\x62\x61\x63kground_color\x18\x12 \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x10\x88\x01\x01\x12\x19\n\x0c\x63ulling_mask\x18\x13 \x01(\x05H\x11\x88\x01\x01\x12I\n\x17\x63ustom_baked_texture_id\x18\x14 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x12\x88\x01\x01\x12\x42\n\x10\x62\x61ked_texture_id\x18\x15 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x13\x88\x01\x01\x42\n\n\x08_enabledB\x07\n\x05_modeB\x0f\n\r_refresh_modeB\x14\n\x12_time_slicing_modeB\x0e\n\x0c_clear_flagsB\r\n\x0b_importanceB\x0c\n\n_intensityB\x12\n\x10_near_clip_planeB\x11\n\x0f_far_clip_planeB\x19\n\x17_render_dynamic_objectsB\x11\n\x0f_box_projectionB\x11\n\x0f_blend_distanceB\t\n\x07_boundsB\r\n\x0b_resolutionB\x06\n\x04_hdrB\x12\n\x10_shadow_distanceB\x13\n\x11_background_colorB\x0f\n\r_culling_maskB\x1a\n\x18_custom_baked_texture_idB\x13\n\x11_baked_texture_id*|\n\x13ReflectionProbeMode\x12\x1f\n\x1bREFLECTION_PROBE_MODE_BAKED\x10\x00\x12 \n\x1cREFLECTION_PROBE_MODE_CUSTOM\x10\x01\x12\"\n\x1eREFLECTION_PROBE_MODE_REALTIME\x10\x02*r\n\x19ReflectionProbeClearFlags\x12'\n#REFLECTION_PROBE_CLEAR_FLAGS_SKYBOX\x10\x00\x12,\n(REFLECTION_PROBE_CLEAR_FLAGS_SOLID_COLOR\x10\x01*\xa8\x01\n\x1aReflectionProbeRefreshMode\x12*\n&REFLECTION_PROBE_REFRESH_MODE_ON_AWAKE\x10\x00\x12-\n)REFLECTION_PROBE_REFRESH_MODE_EVERY_FRAME\x10\x01\x12/\n+REFLECTION_PROBE_REFRESH_MODE_VIA_SCRIPTING\x10\x02*\xcb\x01\n\x1eReflectionProbeTimeSlicingMode\x12\x38\n4REFLECTION_PROBE_TIME_SLICING_MODE_ALL_FACES_AT_ONCE\x10\x00\x12\x37\n3REFLECTION_PROBE_TIME_SLICING_MODE_INDIVIDUAL_FACES\x10\x01\x12\x36\n2REFLECTION_PROBE_TIME_SLICING_MODE_NO_TIME_SLICING\x10\x02\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "unity.reflection_probe_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\022PLUME.Sample.Unity"
    _globals["_REFLECTIONPROBEMODE"]._serialized_start = 1573
    _globals["_REFLECTIONPROBEMODE"]._serialized_end = 1697
    _globals["_REFLECTIONPROBECLEARFLAGS"]._serialized_start = 1699
    _globals["_REFLECTIONPROBECLEARFLAGS"]._serialized_end = 1813
    _globals["_REFLECTIONPROBEREFRESHMODE"]._serialized_start = 1816
    _globals["_REFLECTIONPROBEREFRESHMODE"]._serialized_end = 1984
    _globals["_REFLECTIONPROBETIMESLICINGMODE"]._serialized_start = 1987
    _globals["_REFLECTIONPROBETIMESLICINGMODE"]._serialized_end = 2190
    _globals["_REFLECTIONPROBECREATE"]._serialized_start = 118
    _globals["_REFLECTIONPROBECREATE"]._serialized_end = 194
    _globals["_REFLECTIONPROBEDESTROY"]._serialized_start = 196
    _globals["_REFLECTIONPROBEDESTROY"]._serialized_end = 273
    _globals["_REFLECTIONPROBEUPDATE"]._serialized_start = 276
    _globals["_REFLECTIONPROBEUPDATE"]._serialized_end = 1571
# @@protoc_insertion_point(module_scope)
