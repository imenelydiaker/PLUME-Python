# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/camera.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12unity/camera.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x15unity/rendering.proto\x1a\x14\x63ommon/vector2.proto\x1a\x14\x63ommon/vector3.proto\x1a\x16\x63ommon/matrix4x4.proto\x1a\x12\x63ommon/color.proto\x1a\x11\x63ommon/rect.proto"C\n\x0c\x43\x61meraCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier"D\n\rCameraDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier"\xc1\x16\n\x0c\x43\x61meraUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x1c\n\x0fnear_clip_plane\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0e\x66\x61r_clip_plane\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x1a\n\rfield_of_view\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12>\n\x0erendering_path\x18\x05 \x01(\x0e\x32!.plume.sample.unity.RenderingPathH\x03\x88\x01\x01\x12\x16\n\tallow_hdr\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12\x17\n\nallow_msaa\x18\x07 \x01(\x08H\x05\x88\x01\x01\x12%\n\x18\x61llow_dynamic_resolution\x18\x08 \x01(\x08H\x06\x88\x01\x01\x12&\n\x19\x66orce_into_render_texture\x18\t \x01(\x08H\x07\x88\x01\x01\x12\x1e\n\x11orthographic_size\x18\n \x01(\x02H\x08\x88\x01\x01\x12\x19\n\x0corthographic\x18\x0b \x01(\x08H\t\x88\x01\x01\x12\x41\n\x10opaque_sort_mode\x18\x0c \x01(\x0e\x32".plume.sample.unity.OpaqueSortModeH\n\x88\x01\x01\x12M\n\x16transparency_sort_mode\x18\r \x01(\x0e\x32(.plume.sample.unity.TransparencySortModeH\x0b\x88\x01\x01\x12\x41\n\x16transparency_sort_axis\x18\x0e \x01(\x0b\x32\x1c.plume.sample.common.Vector3H\x0c\x88\x01\x01\x12\x12\n\x05\x64\x65pth\x18\x0f \x01(\x02H\r\x88\x01\x01\x12\x13\n\x06\x61spect\x18\x10 \x01(\x02H\x0e\x88\x01\x01\x12\x19\n\x0c\x63ulling_mask\x18\x11 \x01(\x05H\x0f\x88\x01\x01\x12\x17\n\nevent_mask\x18\x12 \x01(\x05H\x10\x88\x01\x01\x12!\n\x14layer_cull_spherical\x18\x13 \x01(\x08H\x11\x88\x01\x01\x12\x18\n\x0b\x63\x61mera_type\x18\x14 \x01(\rH\x12\x88\x01\x01\x12O\n\x14layer_cull_distances\x18\x15 \x01(\x0b\x32,.plume.sample.unity.CameraLayerCullDistancesH\x13\x88\x01\x01\x12"\n\x15use_occlusion_culling\x18\x16 \x01(\x08H\x14\x88\x01\x01\x12;\n\x0e\x63ulling_matrix\x18\x17 \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H\x15\x88\x01\x01\x12\x39\n\x10\x62\x61\x63kground_color\x18\x18 \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x16\x88\x01\x01\x12\x18\n\x0b\x63lear_flags\x18\x19 \x01(\rH\x17\x88\x01\x01\x12\x1f\n\x12\x64\x65pth_texture_mode\x18\x1a \x01(\rH\x18\x88\x01\x01\x12.\n!clear_stencil_after_lighting_pass\x18\x1b \x01(\x08H\x19\x88\x01\x01\x12$\n\x17use_physical_properties\x18\x1c \x01(\x08H\x1a\x88\x01\x01\x12\x36\n\x0bsensor_size\x18\x1d \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x1b\x88\x01\x01\x12\x35\n\nlens_shift\x18\x1e \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x1c\x88\x01\x01\x12\x19\n\x0c\x66ocal_length\x18\x1f \x01(\x02H\x1d\x88\x01\x01\x12<\n\x08gate_fit\x18  \x01(\x0e\x32%.plume.sample.unity.CameraGateFitModeH\x1e\x88\x01\x01\x12,\n\x04rect\x18! \x01(\x0b\x32\x19.plume.sample.common.RectH\x1f\x88\x01\x01\x12\x32\n\npixel_rect\x18" \x01(\x0b\x32\x19.plume.sample.common.RectH \x88\x01\x01\x12\x43\n\x11target_texture_id\x18# \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH!\x88\x01\x01\x12\x1b\n\x0etarget_display\x18$ \x01(\x05H"\x88\x01\x01\x12\x43\n\x16world_to_camera_matrix\x18% \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H#\x88\x01\x01\x12>\n\x11projection_matrix\x18& \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H$\x88\x01\x01\x12K\n\x1enon_jittered_projection_matrix\x18\' \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H%\x88\x01\x01\x12\x45\n8use_jittered_projection_matrix_for_transparent_rendering\x18( \x01(\x08H&\x88\x01\x01\x12\x1e\n\x11stereo_separation\x18) \x01(\x02H\'\x88\x01\x01\x12\x1f\n\x12stereo_convergence\x18* \x01(\x02H(\x88\x01\x01\x12M\n\x11stereo_target_eye\x18+ \x01(\x0e\x32-.plume.sample.unity.CameraStereoTargetEyeMaskH)\x88\x01\x01\x42\x12\n\x10_near_clip_planeB\x11\n\x0f_far_clip_planeB\x10\n\x0e_field_of_viewB\x11\n\x0f_rendering_pathB\x0c\n\n_allow_hdrB\r\n\x0b_allow_msaaB\x1b\n\x19_allow_dynamic_resolutionB\x1c\n\x1a_force_into_render_textureB\x14\n\x12_orthographic_sizeB\x0f\n\r_orthographicB\x13\n\x11_opaque_sort_modeB\x19\n\x17_transparency_sort_modeB\x19\n\x17_transparency_sort_axisB\x08\n\x06_depthB\t\n\x07_aspectB\x0f\n\r_culling_maskB\r\n\x0b_event_maskB\x17\n\x15_layer_cull_sphericalB\x0e\n\x0c_camera_typeB\x17\n\x15_layer_cull_distancesB\x18\n\x16_use_occlusion_cullingB\x11\n\x0f_culling_matrixB\x13\n\x11_background_colorB\x0e\n\x0c_clear_flagsB\x15\n\x13_depth_texture_modeB$\n"_clear_stencil_after_lighting_passB\x1a\n\x18_use_physical_propertiesB\x0e\n\x0c_sensor_sizeB\r\n\x0b_lens_shiftB\x0f\n\r_focal_lengthB\x0b\n\t_gate_fitB\x07\n\x05_rectB\r\n\x0b_pixel_rectB\x14\n\x12_target_texture_idB\x11\n\x0f_target_displayB\x19\n\x17_world_to_camera_matrixB\x14\n\x12_projection_matrixB!\n\x1f_non_jittered_projection_matrixB;\n9_use_jittered_projection_matrix_for_transparent_renderingB\x14\n\x12_stereo_separationB\x15\n\x13_stereo_convergenceB\x14\n\x12_stereo_target_eye"-\n\x18\x43\x61meraLayerCullDistances\x12\x11\n\tdistances\x18\x01 \x03(\x02*\xbc\x01\n\x11\x43\x61meraGateFitMode\x12\x1d\n\x19\x43\x41MERA_GATE_FIT_MODE_NONE\x10\x00\x12!\n\x1d\x43\x41MERA_GATE_FIT_MODE_VERTICAL\x10\x01\x12#\n\x1f\x43\x41MERA_GATE_FIT_MODE_HORIZONTAL\x10\x02\x12\x1d\n\x19\x43\x41MERA_GATE_FIT_MODE_FILL\x10\x03\x12!\n\x1d\x43\x41MERA_GATE_FIT_MODE_OVERSCAN\x10\x04*\xbc\x01\n\x19\x43\x61meraStereoTargetEyeMask\x12&\n"CAMERA_STEREO_TARGET_EYE_MASK_NONE\x10\x00\x12&\n"CAMERA_STEREO_TARGET_EYE_MASK_LEFT\x10\x01\x12\'\n#CAMERA_STEREO_TARGET_EYE_MASK_RIGHT\x10\x02\x12&\n"CAMERA_STEREO_TARGET_EYE_MASK_BOTH\x10\x03\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "unity.camera_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\022PLUME.Sample.Unity"
    _globals["_CAMERAGATEFITMODE"]._serialized_start = 3268
    _globals["_CAMERAGATEFITMODE"]._serialized_end = 3456
    _globals["_CAMERASTEREOTARGETEYEMASK"]._serialized_start = 3459
    _globals["_CAMERASTEREOTARGETEYEMASK"]._serialized_end = 3647
    _globals["_CAMERACREATE"]._serialized_start = 197
    _globals["_CAMERACREATE"]._serialized_end = 264
    _globals["_CAMERADESTROY"]._serialized_start = 266
    _globals["_CAMERADESTROY"]._serialized_end = 334
    _globals["_CAMERAUPDATE"]._serialized_start = 337
    _globals["_CAMERAUPDATE"]._serialized_end = 3218
    _globals["_CAMERALAYERCULLDISTANCES"]._serialized_start = 3220
    _globals["_CAMERALAYERCULLDISTANCES"]._serialized_end = 3265
# @@protoc_insertion_point(module_scope)
