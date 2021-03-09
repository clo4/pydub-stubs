from typing import Any, Callable, Optional, TypeVar, overload

_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])
@overload
def register_pydub_effect(fn: _TFunc, name: Optional[str] = ...) -> _TFunc: ...
@overload
def register_pydub_effect(name: str) -> Callable[[_TFunc], _TFunc]: ...
