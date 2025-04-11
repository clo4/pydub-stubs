# pydub-stubs

Pydub version: **0.25.1**

**`pydub-stubs` provides type information for [Pydub].**<br> Only the public
interface is guaranteed to be typed, however there are type definitions for some
private and undocumented functions.

[Pydub]: https://github.com/jiaaro/pydub

```
pip install pydub-stubs
```

<br>

## Anticipated Questions

### Q: What is `_Metadata` and `_PartialMetadata`?

These are legacy types that have been replaced by the `channels`, `frame_rate`,
and `sample_rate` keyword arguments.

<br>

## Changelog

### Version 0.25.1.5

- **Fixed incorrect `WhiteNoise` generator name**<br> Previously, the generator
  was incorrectly named `Whitenoise`.
  ([#7](https://github.com/clo4/pydub-stubs/pull/7) - thanks,
  [@Kakadus](https://github.com/Kakadus)!)

### Version 0.25.1.4

- **Added "effect" functions as methods on `AudioSegment`**<br> The methods have
  always been accessible on AudioSegment, but since they are not defined on the
  class, they were not previously defined in the type stubs. Note that if
  `pydub.scipy_effects` is imported, the effect methods may have slightly
  different definitions.

### Version 0.25.1.3

- **Added `typing.BinaryIO` to `_PathLike`**<br> Pydub supports using an IO
  object in place of a file for both creating and exporting AudioSegments.
  (Fixes [#5](https://github.com/clo4/pydub-stubs/issues/5))

### Version 0.25.1.2

- **Added `pathlib.Path` to `_PathLike`**<br> Allows you to use `Path` objects
  in place of strings. (thanks,
  [@qthequartermasterman](https://github.com/qthequartermasterman)!)

### Version 0.25.1.1

- **Removed literal type fallback overloads**<br> The fallbacks removed all the
  advantages of using literals at all.

- **Modernized the type stubs**<br> Uses new union syntax, and more.
  ([#2](https://github.com/clo4/pydub-stubs/pull/2) and
  [#3](https://github.com/clo4/pydub-stubs/pull/3) - thanks,
  [@Viicos](https://github.com/Viicos)!)

- **Add `WavSubChunk`, `WavData`, and undocumented functions**<br> These
  previously existed and were available but were untyped. (thanks again,
  [@Viicos](https://github.com/Viicos)!)

<details>
<summary>Previous versions</summary>

### Version 0.25.1.0

- **Added v0.25.0 features**<br> This includes `pydub.scipy_effects.eq` and new
  classmethod parameters.

- **Signatures now use literals where possible**<br> Overloaded implementations
  exist as a fallback.

- **Added missing modules**<br> `pydub.silence` and `pydub.utils`

### Version 0.24.1.9

- **Add undocumented parameter of `AudioSegment.from_file`**<br>
  `read_ahead_limit` is absent from the documentation but is a supported keyword
  argument.

### Version 0.24.1.8

- **Export other modules**<br> Adds exports for effects, exceptions, generators,
  playback, and scipy_effects

### Version 0.24.1.7

- **Added `AudioSegment._spawn` (again)**<br> This was accidentally removed in
  an earlier version.

- **Improved `pydub.effects.invert_phase`**<br> This is technically less
  accurate as `(0, 0)` is equivalent to `(0, 1)`.

### Version 0.24.1.6

- **Removed testing symbols from `pydub.audio_segment`**<br>

### Version 0.24.1.5

- **Fixed `AudioSegment.export`**<br> First param is named `out_f` and isn't
  required.

### Version 0.24.1.4

- **Improved signature of `AudioSegment.from_file`**<br> The keyword arguments
  for raw/PCM audio don't require `format` to be set to either `raw` or `pcm`.

- **Fixed package exports**<br> Exports `AudioSegment` from `__init__.py`.

### Version 0.24.1.3

- **Fixed overloads of `AudioSegment.fade`**<br> Exactly two of `start`, `end`,
  and `duration` must be given.

### Version 0.24.1.2

- **Improved `AudioSegment.fade`**<br> Changed to use overloads to prevent
  invalid method calls.

- **Improved `AudioSegment.from_mono_audiosegments`**<br> Use a positional-only
  parameter to ensure there's at least 1 argument.

### Version 0.24.1.1

- **Fixed `AudioSegment.__init__`**<br> Use overloads to model correct
  parameters.

- **Fixed `AudioSegment._spawn`**<br> Parameter `overrides` accepts a partial
  dictionary.

- **Fixed `pydub.scipy_effects.high_pass_filter`**<br> Parameter `order` should
  be `int`, not `float`.

### Version 0.24.1.0

Released

</details>
