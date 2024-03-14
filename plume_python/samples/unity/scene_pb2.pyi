from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadScene(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.SceneIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.SceneIdentifier, _Mapping]] = ...) -> None: ...

class UnloadScene(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.SceneIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.SceneIdentifier, _Mapping]] = ...) -> None: ...

class ChangeActiveScene(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.SceneIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.SceneIdentifier, _Mapping]] = ...) -> None: ...
