# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/tmp_text.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x17unity/ui/tmp_text.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x14\x63ommon/vector4.proto\x1a\x12\x63ommon/color.proto\"D\n\rTMPTextCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"E\n\x0eTMPTextDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\"\x9d\x07\n\rTMPTextUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32'.plume.sample.unity.ComponentIdentifier\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x39\n\x07\x66ont_id\x18\x03 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01\x88\x01\x01\x12\x17\n\nfont_style\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x16\n\tfont_size\x18\x05 \x01(\x02H\x03\x88\x01\x01\x12\x16\n\tauto_size\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12\x1a\n\rfont_size_min\x18\x07 \x01(\x02H\x05\x88\x01\x01\x12\x1a\n\rfont_size_max\x18\x08 \x01(\x02H\x06\x88\x01\x01\x12.\n\x05\x63olor\x18\t \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x07\x88\x01\x01\x12\x1e\n\x11\x63haracter_spacing\x18\n \x01(\x02H\x08\x88\x01\x01\x12\x19\n\x0cword_spacing\x18\x0b \x01(\x02H\t\x88\x01\x01\x12\x19\n\x0cline_spacing\x18\x0c \x01(\x02H\n\x88\x01\x01\x12\x1e\n\x11paragraph_spacing\x18\r \x01(\x02H\x0b\x88\x01\x01\x12\x1d\n\x10wrapping_enabled\x18\x0e \x01(\x08H\x0c\x88\x01\x01\x12\x16\n\talignment\x18\x0f \x01(\x05H\r\x88\x01\x01\x12\x15\n\x08overflow\x18\x10 \x01(\x05H\x0e\x88\x01\x01\x12\x1f\n\x12horizontal_mapping\x18\x11 \x01(\x05H\x0f\x88\x01\x01\x12\x1d\n\x10vertical_mapping\x18\x12 \x01(\x05H\x10\x88\x01\x01\x12\x31\n\x06margin\x18\x13 \x01(\x0b\x32\x1c.plume.sample.common.Vector4H\x11\x88\x01\x01\x42\x07\n\x05_textB\n\n\x08_font_idB\r\n\x0b_font_styleB\x0c\n\n_font_sizeB\x0c\n\n_auto_sizeB\x10\n\x0e_font_size_minB\x10\n\x0e_font_size_maxB\x08\n\x06_colorB\x14\n\x12_character_spacingB\x0f\n\r_word_spacingB\x0f\n\r_line_spacingB\x14\n\x12_paragraph_spacingB\x13\n\x11_wrapping_enabledB\x0c\n\n_alignmentB\x0b\n\t_overflowB\x15\n\x13_horizontal_mappingB\x13\n\x11_vertical_mappingB\t\n\x07_marginB\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "unity.ui.tmp_text_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\025PLUME.Sample.Unity.UI"
    _globals["_TMPTEXTCREATE"]._serialized_start = 114
    _globals["_TMPTEXTCREATE"]._serialized_end = 182
    _globals["_TMPTEXTDESTROY"]._serialized_start = 184
    _globals["_TMPTEXTDESTROY"]._serialized_end = 253
    _globals["_TMPTEXTUPDATE"]._serialized_start = 256
    _globals["_TMPTEXTUPDATE"]._serialized_end = 1181
# @@protoc_insertion_point(module_scope)
