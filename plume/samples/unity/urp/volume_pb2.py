# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/urp/volume.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16unity/urp/volume.proto\x12\x16plume.sample.unity.urp\x1a\x17unity/identifiers.proto\"C\n\x0cVolumeCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"\xd1\x03\n\x0cVolumeUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x16\n\tis_global\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x46\n\tcolliders\x18\x03 \x01(\x0b\x32..plume.sample.unity.urp.VolumeUpdate.CollidersH\x01\x88\x01\x01\x12\x1b\n\x0e\x62lend_distance\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x13\n\x06weight\x18\x05 \x01(\x02H\x03\x88\x01\x01\x12\x15\n\x08priority\x18\x06 \x01(\x02H\x04\x88\x01\x01\x12\x43\n\x11shared_profile_id\x18\x07 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x05\x88\x01\x01\x1a\x41\n\tColliders\x12\x34\n\x03ids\x18\x01 \x03(\x0b\x32\'.plume.sample.unity.ComponentIdentifierB\x0c\n\n_is_globalB\x0c\n\n_collidersB\x11\n\x0f_blend_distanceB\t\n\x07_weightB\x0b\n\t_priorityB\x14\n\x12_shared_profile_id\"[\n\x13VolumeUpdateEnabled\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x42\x19\xaa\x02\x16PLUME.Sample.Unity.URPb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.urp.volume_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\026PLUME.Sample.Unity.URP'
  _globals['_VOLUMECREATE']._serialized_start=75
  _globals['_VOLUMECREATE']._serialized_end=142
  _globals['_VOLUMEUPDATE']._serialized_start=145
  _globals['_VOLUMEUPDATE']._serialized_end=610
  _globals['_VOLUMEUPDATE_COLLIDERS']._serialized_start=452
  _globals['_VOLUMEUPDATE_COLLIDERS']._serialized_end=517
  _globals['_VOLUMEUPDATEENABLED']._serialized_start=612
  _globals['_VOLUMEUPDATEENABLED']._serialized_end=703
# @@protoc_insertion_point(module_scope)
