# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/image.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14unity/ui/image.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"B\n\x0bImageCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"C\n\x0cImageDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"\xc8\x01\n\x0bImageUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12;\n\tsprite_id\x18\x02 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x00\x88\x01\x01\x12\x30\n\x04type\x18\x03 \x01(\x0e\x32\x1d.plume.sample.unity.ImageTypeH\x01\x88\x01\x01\x42\x0c\n\n_sprite_idB\x07\n\x05_type*f\n\tImageType\x12\x15\n\x11IMAGE_TYPE_SIMPLE\x10\x00\x12\x15\n\x11IMAGE_TYPE_SLICED\x10\x01\x12\x14\n\x10IMAGE_TYPE_TILED\x10\x02\x12\x15\n\x11IMAGE_TYPE_FILLED\x10\x03\x42\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.ui.image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025PLUME.Sample.Unity.UI'
  _globals['_IMAGETYPE']._serialized_start=409
  _globals['_IMAGETYPE']._serialized_end=511
  _globals['_IMAGECREATE']._serialized_start=69
  _globals['_IMAGECREATE']._serialized_end=135
  _globals['_IMAGEDESTROY']._serialized_start=137
  _globals['_IMAGEDESTROY']._serialized_end=204
  _globals['_IMAGEUPDATE']._serialized_start=207
  _globals['_IMAGEUPDATE']._serialized_end=407
# @@protoc_insertion_point(module_scope)
