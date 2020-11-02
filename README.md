# pydub-stubs

Pydub version: **0.24.1**

**`pydub-stubs` provides type information for Pydub.**<br>
Only the public interface is guaranteed to be typed.

```
pip install pydub-stubs
```

<br>

## Aniticipated Questions

### Q: Why is <code>AudioSegment.<i>some_effect(...)</i></code> missing?

**TL;DR:** Import it as a function from `pydub.effects`.

Pydub dynamically adds certain functions to `AudioSegment` at runtime.
This is easy to type, but impossible to be 100% safe about.

A great example of why this can is difficult is `pydub.scipy_effects`,
which registers two effects that are named identically to those in
`pydub.effects`, but have different signatures. Importing this module
will override the previous effects, so now the signatures are wrong.

### Q: What the hell is that version number?

`major.minor.patch.stubs`, where major/minor/patch are the latest
supported Pydub version. The stubs version being last means pinning
to a specific Pydub version will always get the latest stubs available.

<br>

## Changelog

### Version 0.24.1.5

* **Fix `AudioSegment.export`**
  First param is named `out_f` and isn't required.

<details>
<summary>Previous versions</summary>

### Version 0.24.1.4

* **Improved signature of `AudioSegment.from_file`**<br>
  The keyword arguments for raw/PCM audio don't require `format` to be
  set to either `raw` or `pcm`.

* **Fix package exports**<br>
  Exports `AudioSegment` from `__init__.py`.

### Version 0.24.1.3

* **Fixed overloads of `AudioSegment.fade`**<br>
  Exactly two of `start`, `end`, and `duration` must be given.

### Version 0.24.1.2

* **Improved `AudioSegment.fade`**<br>
  Changed to use overloads to prevent invalid method calls.

* **Improved `AudioSegment.from_mono_audiosegments`**<br>
  Use a positional-only parameter to ensure there's at least 1 argument.

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
