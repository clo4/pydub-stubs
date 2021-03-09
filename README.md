# pydub-stubs

Pydub version: **0.25.0**

**`pydub-stubs` provides type information for [Pydub].**<br>
Only the public interface is guaranteed to be typed.

[Pydub]: https://github.com/jiaaro/pydub

```
pip install pydub-stubs
```

<br>

## Anticipated Questions

### Q: Why is <code>AudioSegment.<i>effect(...)</i></code> missing?

**TL;DR:** Import it as a function from `pydub.effects`.

Pydub adds methods to `AudioSegment` at runtime, which means it's
easier to modularize but also means there's no guarantee that a
method signature is correct.

For example, `pydub.scipy_effects` overwrites two methods from
`pydub.effects` with different signatures.

### Q: What is `Metadata` and `PartialMetadata`?

Pydub originally used dictionaries when creating an AudioSegment.
`Metadata` and `PartialMetadata` do not exist at runtime. Using these
is no longer recommended, but they're still supported and used
internally. You can use the `channels`, `frame_rate`, and
`sample_rate` keyword arguments.

<br>

## Changelog

### Version 0.25.0.0

* **Add v0.25.0 features**<br>
  This includes `pydub.scipy_effects.eq` and new classmethod
  parameters.

* **Use literals in signatures**<br>
  Literals are now used where possible, with fallback overloads.

* **Add `pydub.silence`**<br>
  Documentation was added in v0.25.0, so it looks to be part of the
  API.

* **Add `pydub.utils`**<br>
  Currently only has `register_pydub_effect`.

<details>
<summary>Previous versions</summary>

### Version 0.24.1.9

* **Add undocumented parameter of `AudioSegment.from_file`**<br>
  `read_ahead_limit` is absent from the documentation but is a
  supported keyword argument.

### Version 0.24.1.8

* **Export other modules**<br>
  Adds exports for effects, exceptions, generators, playback, and
  scipy_effects

### Version 0.24.1.7

* **Add `AudioSegment._spawn` (again)**<br>
  This was accidentally removed in an earlier version.

* **Improve `pydub.effects.invert_phase`**<br>
  This is technically less accurate as `(0, 0)` is equivalent
  to `(0, 1)`.

### Version 0.24.1.6

* **Remove testing symbols from `pydub.audio_segment`**<br>

### Version 0.24.1.5

* **Fix `AudioSegment.export`**<br>
  First param is named `out_f` and isn't required.

### Version 0.24.1.4

* **Improved signature of `AudioSegment.from_file`**<br>
  The keyword arguments for raw/PCM audio don't require `format` to
  be set to either `raw` or `pcm`.

* **Fix package exports**<br>
  Exports `AudioSegment` from `__init__.py`.

### Version 0.24.1.3

* **Fixed overloads of `AudioSegment.fade`**<br>
  Exactly two of `start`, `end`, and `duration` must be given.

### Version 0.24.1.2

* **Improved `AudioSegment.fade`**<br>
  Changed to use overloads to prevent invalid method calls.

* **Improved `AudioSegment.from_mono_audiosegments`**<br>
  Use a positional-only parameter to ensure there's at least 1
  argument.

### Version 0.24.1.1

* **Fixed `AudioSegment.__init__`**<br>
  Use overloads to model correct parameters.

* **Fixed `AudioSegment._spawn`**<br>
  Parameter `overrides` accepts a partial dictionary.

* **Fixed `pydub.scipy_effects.high_pass_filter`**<br>
  Parameter `order` should be `int`, not `float`.

### Version 0.24.1.0

Released

</details>
