from __future__ import annotations

from .audio_segment import AudioSegment

def low_pass_filter(
    seg: AudioSegment,
    cutoff_freq: float,
    order: int = ...,
) -> AudioSegment: ...
def high_pass_filter(
    seg: AudioSegment,
    cutoff_freq: float,
    order: int = ...,
) -> AudioSegment: ...
def band_pass_filter(
    seg: AudioSegment,
    low_cutoff_freq: float,
    high_cutoff_freq: float,
    order: int = ...,
) -> AudioSegment: ...
