from __future__ import annotations
from typing import Literal, overload
from .audio_segment import AudioSegment
@overload
def eq(
    seg: AudioSegment,
    focus_freq: int,
    bandwidth: int = ...,
    channel_mode: Literal["L+R", "L", "R", "M+S", "M", "S"] = ...,
    filter_mode: Literal["peak", "low_shelf", "high_shelf"] = ...,
    gain_dB: int = ...,
    order: int = ...,
) -> AudioSegment: ...
@overload
def eq(
    seg: AudioSegment,
    focus_freq: int,
    bandwidth: int = ...,
    channel_mode: str = ...,
    filter_mode: str = ...,
    gain_dB: int = ...,
    order: int = ...,
) -> AudioSegment: ...
def low_pass_filter(seg: AudioSegment, cutoff_freq: float, order: int = ...) -> AudioSegment: ...
def high_pass_filter(seg: AudioSegment, cutoff_freq: float, order: int = ...) -> AudioSegment: ...
def band_pass_filter(seg: AudioSegment, low_cutoff_freq: float, high_cutoff_freq: float, order: int = ...) -> AudioSegment: ...
