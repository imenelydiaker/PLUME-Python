# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/xritk/xr_base_interactable.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&unity/xritk/xr_base_interactable.proto\x12\x18plume.sample.unity.xritk\x1a\x17unity/identifiers.proto\"O\n\x18XRBaseInteractableCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"P\n\x19XRBaseInteractableDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"d\n\x1cXRBaseInteractableSetEnabled\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xa2\x01\n\x1cXRBaseInteractableHoverEnter\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa1\x01\n\x1bXRBaseInteractableHoverExit\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa3\x01\n\x1dXRBaseInteractableSelectEnter\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa2\x01\n\x1cXRBaseInteractableSelectExit\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa5\x01\n\x1fXRBaseInteractableActivateEnter\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifier\"\xa4\x01\n\x1eXRBaseInteractableActivateExit\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12M\n\x12interactor_current\x18\x02 \x01(\x0b\x32\x31.plume.sample.unity.TransformGameObjectIdentifierB\x1b\xaa\x02\x18PLUME.Sample.Unity.XRITKb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.xritk.xr_base_interactable_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\030PLUME.Sample.Unity.XRITK'
  _globals['_XRBASEINTERACTABLECREATE']._serialized_start=93
  _globals['_XRBASEINTERACTABLECREATE']._serialized_end=172
  _globals['_XRBASEINTERACTABLEDESTROY']._serialized_start=174
  _globals['_XRBASEINTERACTABLEDESTROY']._serialized_end=254
  _globals['_XRBASEINTERACTABLESETENABLED']._serialized_start=256
  _globals['_XRBASEINTERACTABLESETENABLED']._serialized_end=356
  _globals['_XRBASEINTERACTABLEHOVERENTER']._serialized_start=359
  _globals['_XRBASEINTERACTABLEHOVERENTER']._serialized_end=521
  _globals['_XRBASEINTERACTABLEHOVEREXIT']._serialized_start=524
  _globals['_XRBASEINTERACTABLEHOVEREXIT']._serialized_end=685
  _globals['_XRBASEINTERACTABLESELECTENTER']._serialized_start=688
  _globals['_XRBASEINTERACTABLESELECTENTER']._serialized_end=851
  _globals['_XRBASEINTERACTABLESELECTEXIT']._serialized_start=854
  _globals['_XRBASEINTERACTABLESELECTEXIT']._serialized_end=1016
  _globals['_XRBASEINTERACTABLEACTIVATEENTER']._serialized_start=1019
  _globals['_XRBASEINTERACTABLEACTIVATEENTER']._serialized_end=1184
  _globals['_XRBASEINTERACTABLEACTIVATEEXIT']._serialized_start=1187
  _globals['_XRBASEINTERACTABLEACTIVATEEXIT']._serialized_end=1351
# @@protoc_insertion_point(module_scope)
