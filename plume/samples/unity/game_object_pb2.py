# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/game_object.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17unity/game_object.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"D\n\x10GameObjectCreate\x12\x30\n\x02id\x18\x01 \x01(\x0b\x32$.plume.sample.unity.ObjectIdentifier\"E\n\x11GameObjectDestroy\x12\x30\n\x02id\x18\x01 \x01(\x0b\x32$.plume.sample.unity.ObjectIdentifier\"\xdc\x01\n\x10GameObjectUpdate\x12\x30\n\x02id\x18\x01 \x01(\x0b\x32$.plume.sample.unity.ObjectIdentifier\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x61\x63tive\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12\x10\n\x03tag\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05layer\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x15\n\x08scene_id\x18\x06 \x01(\x05H\x04\x88\x01\x01\x42\x07\n\x05_nameB\t\n\x07_activeB\x06\n\x04_tagB\x08\n\x06_layerB\x0b\n\t_scene_idB\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.game_object_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_GAMEOBJECTCREATE']._serialized_start=72
  _globals['_GAMEOBJECTCREATE']._serialized_end=140
  _globals['_GAMEOBJECTDESTROY']._serialized_start=142
  _globals['_GAMEOBJECTDESTROY']._serialized_end=211
  _globals['_GAMEOBJECTUPDATE']._serialized_start=214
  _globals['_GAMEOBJECTUPDATE']._serialized_end=434
# @@protoc_insertion_point(module_scope)
