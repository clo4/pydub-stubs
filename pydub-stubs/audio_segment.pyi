from __future__ import annotations

import array
import os
from typing import (
    Any,
    ClassVar,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Sequence,
    TypedDict,
    Union,
    BinaryIO,
    overload,
)

PathLike = Union[str, bytes, os.PathLike[Any]]

class OverrideDict(TypedDict, final=False):
    sample_width: int
    frame_rate: int
    frame_width: int
    channels: int

# If it's typed as float, it's probably decibels. If it's int, it's
# usually either milliseconds or hertz (whatever's logical)
class AudioSegment:
    converter: ClassVar[str]
    DEFAULT_CODECS: ClassVar[Dict[str, str]]
    def __init__(
        self,
        data: Optional[Union[bytes, array.array[int]]] = ...,
        *,
        sample_width: Optional[int] = ...,
        frame_rate: Optional[int] = ...,
        channels: Optional[int] = ...,
    ) -> None: ...
    def _spawn(
        self,
        data: Union[bytes, array.array[int], BinaryIO, List[bytes]],
        overrides: OverrideDict = ...,
    ) -> AudioSegment: ...
    def __add__(self, arg: Union[float, AudioSegment]) -> AudioSegment: ...
    def __radd__(self, rarg: AudioSegment) -> AudioSegment: ...
    def __sub__(self, arg: float) -> AudioSegment: ...
    def __mul__(self, arg: Union[int, AudioSegment]) -> AudioSegment: ...
    def __len__(self) -> int: ...
    def __getitem__(self, ms: Union[int, slice]) -> AudioSegment: ...
    def __iter__(self) -> Iterator[AudioSegment]: ...
    @property
    def channels(self) -> int: ...
    @property
    def sample_width(self) -> int: ...
    @property
    def frame_rate(self) -> int: ...
    @property
    def frame_width(self) -> int: ...
    @property
    def rms(self) -> float: ...
    @property
    def max(self) -> float: ...
    @property
    def dBFS(self) -> float: ...
    @property
    def max_dBFS(self) -> float: ...
    @property
    def max_possible_amplitude(self) -> float: ...
    @property
    def duration_seconds(self) -> int: ...
    @property
    def raw_data(self) -> bytes: ...
    @property
    def array_type(self) -> Literal["b", "B", "h", "H", "i", "I"]: ...
    def export(
        self,
        file: PathLike,
        *,
        format: Optional[str] = ...,
        codec: Optional[str] = ...,
        bitrate: Optional[str] = ...,
        tags: Optional[Dict[str, str]] = ...,
        parameters: Optional[Sequence[str]] = ...,
        id3v2_version: Optional[Literal["3", "4"]] = ...,
        cover: Optional[str] = ...,
    ) -> BinaryIO: ...
    def frame_count(self, ms: int = ...) -> float: ...
    def get_frame(self, index: int) -> bytes: ...
    def get_sample_slice(
        self,
        start_sample: Optional[int] = ...,
        end_sample: Optional[int] = ...,
    ) -> AudioSegment: ...
    def append(self, seg: AudioSegment, *, crossfade: int = ...) -> AudioSegment: ...
    def overlay(
        self,
        seg: AudioSegment,
        *,
        position: int = ...,
        loop: bool = ...,
        times: Optional[int] = ...,
        gain_during_overlay: int = ...,
    ) -> AudioSegment: ...
    def apply_gain(self, volume_change: int) -> AudioSegment: ...
    def fade(
        self,
        *,
        start: Optional[int] = ...,
        end: Optional[int] = ...,
        duration: Optional[int] = ...,
        to_gain: float = ...,
        from_gain: float = ...,
    ) -> AudioSegment: ...
    def fade_out(self, duration: int) -> AudioSegment: ...
    def fade_in(self, duration: int) -> AudioSegment: ...
    def reverse(self) -> AudioSegment: ...
    def set_sample_width(self, sample_width: int) -> AudioSegment: ...
    def set_frame_rate(self, frame_rate: int) -> AudioSegment: ...
    def set_channels(self, channels: int) -> AudioSegment: ...
    def split_to_mono(self) -> List[AudioSegment]: ...
    def get_array_of_samples(
        self,
        array_type_override: Optional[
            Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
        ] = ...,
    ) -> array.array[int]: ...
    def get_dc_offset(self, channel: Literal[1, 2]) -> int: ...
    def remove_dc_offset(
        self,
        channel: Optional[Literal[1, 2]] = ...,
        offset: Optional[float] = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file(
        cls,
        file: PathLike,
        *,
        format: Literal["raw", "pcm"],
        frame_rate: int,
        channels: int,
        sample_width: int,
        codec: Optional[str] = ...,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file(
        cls,
        file: PathLike,
        *,
        format: Optional[str] = ...,
        codec: Optional[str] = ...,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file_using_temporary_files(
        cls,
        file: PathLike,
        *,
        format: Literal["raw", "pcm"],
        frame_rate: int,
        channels: int,
        sample_width: int,
        codec: Optional[str] = ...,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file_using_temporary_files(
        cls,
        file: PathLike,
        *,
        format: str = ...,
        codec: Optional[str] = ...,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_mp3(
        cls,
        file: PathLike,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_flv(
        cls,
        file: PathLike,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_ogg(
        cls,
        file: PathLike,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_wav(
        cls,
        file: PathLike,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_raw(
        cls,
        file: PathLike,
        *,
        frame_rate: int,
        channels: int,
        sample_width: int,
        parameters: Optional[Sequence[str]] = ...,
    ) -> AudioSegment: ...
    @classmethod
    def empty(cls) -> AudioSegment: ...
    @classmethod
    def silent(
        cls,
        duration: int = ...,
        frame_rate: int = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_mono_audiosegments(
        cls,
        *mono_segments: AudioSegment,
    ) -> AudioSegment: ...
