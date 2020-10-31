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
will override the previous effects, so the signatures are now wrong.

### Q: What the hell is that version number?

`major.minor.patch.stubs`, where major/minor/patch are the latest
supported Pydub version. The stubs version being last means pinning
to a specific Pydub version will always get the latest stubs available.

<br>

## Changelog

### Version 0.24.1.1

* **Fixed `AudioSegment.__init__`**<br>
  Use overloads to model correct parameters.

* **Fixed `AudioSegment._spawn`**<br>
  Parameter `overrides` accepts a partial dictionary.

* **Fixed `pydub.scipy_effects.high_pass_filter`**<br>
  Parameter `order` should be `int`, not `float`.

<details>
<summary>Previous versions</summary>

### Version 0.24.1.0

Released

</details>
