# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/xritk/xr_base_interactor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$unity/xritk/xr_base_interactor.proto\x12\x18plume.sample.unity.xritk\x1a\x17unity/identifiers.proto\"M\n\x16XRBaseInteractorCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"N\n\x17XRBaseInteractorDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"b\n\x1aXRBaseInteractorSetEnabled\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xa2\x01\n\x1aXRBaseInteractorHoverEnter\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12O\n\x14interactable_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa1\x01\n\x19XRBaseInteractorHoverExit\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12O\n\x14interactable_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa3\x01\n\x1bXRBaseInteractorSelectEnter\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12O\n\x14interactable_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa2\x01\n\x1aXRBaseInteractorSelectExit\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12O\n\x14interactable_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifierB\x1b\xaa\x02\x18PLUME.Sample.Unity.XRITKb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.xritk.xr_base_interactor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\030PLUME.Sample.Unity.XRITK'
  _globals['_XRBASEINTERACTORCREATE']._serialized_start=91
  _globals['_XRBASEINTERACTORCREATE']._serialized_end=168
  _globals['_XRBASEINTERACTORDESTROY']._serialized_start=170
  _globals['_XRBASEINTERACTORDESTROY']._serialized_end=248
  _globals['_XRBASEINTERACTORSETENABLED']._serialized_start=250
  _globals['_XRBASEINTERACTORSETENABLED']._serialized_end=348
  _globals['_XRBASEINTERACTORHOVERENTER']._serialized_start=351
  _globals['_XRBASEINTERACTORHOVERENTER']._serialized_end=513
  _globals['_XRBASEINTERACTORHOVEREXIT']._serialized_start=516
  _globals['_XRBASEINTERACTORHOVEREXIT']._serialized_end=677
  _globals['_XRBASEINTERACTORSELECTENTER']._serialized_start=680
  _globals['_XRBASEINTERACTORSELECTENTER']._serialized_end=843
  _globals['_XRBASEINTERACTORSELECTEXIT']._serialized_start=846
  _globals['_XRBASEINTERACTORSELECTEXIT']._serialized_end=1008
# @@protoc_insertion_point(module_scope)
