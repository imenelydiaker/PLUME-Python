# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/rect_transform.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import vector2_pb2 as common_dot_vector2__pb2
from common import vector3_pb2 as common_dot_vector3__pb2
from common import quaternion_pb2 as common_dot_quaternion__pb2
from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aunity/rect_transform.proto\x12\x12plume.sample.unity\x1a\x14\x63ommon/vector2.proto\x1a\x14\x63ommon/vector3.proto\x1a\x17\x63ommon/quaternion.proto\x1a\x17unity/identifiers.proto\"T\n\x13RectTransformCreate\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"U\n\x14RectTransformDestroy\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"w\n\x1fRectTransformUpdateSiblingIndex\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x15\n\rsibling_index\x18\x02 \x01(\x05\"\xb3\x01\n\x19RectTransformUpdateParent\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12I\n\tparent_id\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifierH\x00\x88\x01\x01\x42\x0c\n\n_parent_id\"\xc8\x01\n\x1bRectTransformUpdatePosition\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x34\n\x0elocal_position\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector3\x12\x34\n\x0eworld_position\x18\x03 \x01(\x0b\x32\x1c.plume.sample.common.Vector3\"\xce\x01\n\x1bRectTransformUpdateRotation\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x37\n\x0elocal_rotation\x18\x02 \x01(\x0b\x32\x1f.plume.sample.common.Quaternion\x12\x37\n\x0eworld_rotation\x18\x03 \x01(\x0b\x32\x1f.plume.sample.common.Quaternion\"\xbf\x01\n\x18RectTransformUpdateScale\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x31\n\x0blocal_scale\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector3\x12\x31\n\x0bworld_scale\x18\x03 \x01(\x0b\x32\x1c.plume.sample.common.Vector3\"\xbf\x01\n\x1aRectTransformUpdateAnchors\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x30\n\nanchor_min\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector2\x12\x30\n\nanchor_max\x18\x03 \x01(\x0b\x32\x1c.plume.sample.common.Vector2\"\x8a\x01\n\x17RectTransformUpdateSize\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12\x30\n\nsize_delta\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector2\"\x86\x01\n\x18RectTransformUpdatePivot\x12=\n\x02id\x18\x01 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\x12+\n\x05pivot\x18\x02 \x01(\x0b\x32\x1c.plume.sample.common.Vector2B\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.rect_transform_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_RECTTRANSFORMCREATE']._serialized_start=144
  _globals['_RECTTRANSFORMCREATE']._serialized_end=228
  _globals['_RECTTRANSFORMDESTROY']._serialized_start=230
  _globals['_RECTTRANSFORMDESTROY']._serialized_end=315
  _globals['_RECTTRANSFORMUPDATESIBLINGINDEX']._serialized_start=317
  _globals['_RECTTRANSFORMUPDATESIBLINGINDEX']._serialized_end=436
  _globals['_RECTTRANSFORMUPDATEPARENT']._serialized_start=439
  _globals['_RECTTRANSFORMUPDATEPARENT']._serialized_end=618
  _globals['_RECTTRANSFORMUPDATEPOSITION']._serialized_start=621
  _globals['_RECTTRANSFORMUPDATEPOSITION']._serialized_end=821
  _globals['_RECTTRANSFORMUPDATEROTATION']._serialized_start=824
  _globals['_RECTTRANSFORMUPDATEROTATION']._serialized_end=1030
  _globals['_RECTTRANSFORMUPDATESCALE']._serialized_start=1033
  _globals['_RECTTRANSFORMUPDATESCALE']._serialized_end=1224
  _globals['_RECTTRANSFORMUPDATEANCHORS']._serialized_start=1227
  _globals['_RECTTRANSFORMUPDATEANCHORS']._serialized_end=1418
  _globals['_RECTTRANSFORMUPDATESIZE']._serialized_start=1421
  _globals['_RECTTRANSFORMUPDATESIZE']._serialized_end=1559
  _globals['_RECTTRANSFORMUPDATEPIVOT']._serialized_start=1562
  _globals['_RECTTRANSFORMUPDATEPIVOT']._serialized_end=1696
# @@protoc_insertion_point(module_scope)