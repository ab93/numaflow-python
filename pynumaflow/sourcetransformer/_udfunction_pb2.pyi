from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from typing import (
    ClassVar as _ClassVar,
    Optional as _Optional,
    List,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ReadyResponse(_message.Message):
    __slots__ = ["ready"]
    READY_FIELD_NUMBER: _ClassVar[int]
    ready: bool

    def __init__(self, ready: _Optional[bool] = ...) -> None: ...

class EventTime(_message.Message):
    __slots__ = ["event_time"]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp

    def __init__(self, event_time: _Optional[_timestamp_pb2.Timestamp] = ...) -> None: ...

class Watermark(_message.Message):
    __slots__ = ["watermark"]
    WATERMARK_FIELD_NUMBER: _ClassVar[int]
    watermark: _timestamp_pb2.Timestamp

    def __init__(self, watermark: _Optional[_timestamp_pb2.Timestamp] = ...) -> None: ...

class Datum(_message.Message):
    __slots__ = ["keys", "value", "event_time", "watermark"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: bytes
    event_time: _timestamp_pb2.Timestamp
    watermark: _timestamp_pb2.Timestamp

    def __init__(
        self,
        keys: _Optional[List[str]],
        value: _Optional[bytes],
        event_time: _Optional[_timestamp_pb2.Timestamp] = ...,
        watermark: _Optional[_timestamp_pb2.Timestamp] = ...,
    ) -> None: ...

class DatumList(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: List[Datum]

    def __init__(self, elements: _Optional[List[Datum]]) -> None: ...
