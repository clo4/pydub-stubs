from typing import Any, Callable, Literal, Optional, TypeVar, Union, overload

from .audio_segment import AudioSegment

_AudioSegmentT = TypeVar("_AudioSegmentT", bound=AudioSegment)
_T = TypeVar("_T")
_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])

@overload
def register_pydub_effect(fn: _TFunc, name: Optional[str] = ...) -> _TFunc: ...
@overload
def register_pydub_effect(name: str) -> Callable[[_TFunc], _TFunc]: ...
@overload
def get_frame_width(bit_depth: Literal[8, 16, 32]) -> Literal[1, 2, 4]: ...
@overload  # fallback
def get_frame_width(bit_depth: int) -> Literal[1, 2, 4]: ...
@overload
def get_array_type(bit_depth: Literal[8, 16, 32], signed: bool = ...) -> Literal["b", "h", "i", "B", "H", "I"]: ...
@overload  # fallback
def get_array_type(bit_depth: int, signed: bool = ...) -> Literal["b", "h", "i", "B", "H", "I"]: ...
@overload
def get_min_max_value(
    bit_depth: Literal[8, 16, 32],
) -> Union[
    tuple[Literal[-0x80], Literal[0x7F]],
    tuple[Literal[-0x8000], Literal[0x7FFF]],
    tuple[Literal[-0x80000000], Literal[0x7FFFFFFF]],
]: ...
@overload  # fallback
def get_min_max_value(
    bit_depth: int,
) -> Union[
    tuple[Literal[-0x80], Literal[0x7F]],
    tuple[Literal[-0x8000], Literal[0x7FFF]],
    tuple[Literal[-0x80000000], Literal[0x7FFFFFFF]],
]: ...
def db_to_float(db: float, using_amplitude: bool = ...) -> float: ...
def ratio_to_db(ratio: float, val2: Optional[float] = ..., using_amplitude: bool = ...) -> float: ...
def make_chunks(audio_segment: _AudioSegmentT, chunk_length: float) -> list[_AudioSegmentT]: ...
def which(program: str) -> str: ...
def get_extra_info(stderr: str) -> dict[int, list[str]]: ...
def mediainfo_json(filepath: str, read_ahead_limit: int = ...) -> dict[str, Any]: ...
def mediainfo(filepath: str) -> dict[str, str]: ...
def cache_codecs(function: Callable[[], _T]) -> Callable[[], _T]: ...
def get_encoder_name() -> Literal["ffmpeg", "avconv"]: ...
def get_player_name() -> Literal["ffplay", "avplay"]: ...
def get_prober_name() -> Literal["ffprobe", "avprobe"]: ...
def get_supported_codecs() -> tuple[set[str], set[str]]: ...
def stereo_to_ms(audio_segment: AudioSegment) -> AudioSegment: ...
def ms_to_stereo(audio_segment: AudioSegment) -> AudioSegment: ...
