from __future__ import annotations
from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Generator
from typing import Any, Iterable, Protocol, TypeVar, AbstractSet, Optional, Union

_T = TypeVar("_T")
_KT = TypeVar("_KT")  # Key type.
_VT = TypeVar("_VT")  # Value type.
_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)

class SupportsKeysAndItems(Protocol[_KT_co, _VT_co]):
    def keys(self) -> Iterable[_KT]: ...
    def items(self) -> AbstractSet[tuple[_KT_co, _VT_co]]: ...

class OrderedMultiDict(dict[_KT, _VT]):
    def __init__(self, *args, **kwargs) -> None: ...
    def add(self, k: _KT, v: Incomplete) -> None: ...
    def addlist(self, k: _KT, v: Iterable) -> None: ...
    def get(self, k: _KT, default: Union[_VT, _T] = ...) -> Union[_VT, _T]: ...
    def getlist(self, k: str, default: Incomplete =...): ...
    def clear(self) -> None: ...
    def setdefault(self, k: _KT, default: _VT = ...) -> _VT: ...
    def copy(self): ...
    @classmethod
    def fromkeys(cls, keys: Iterable, default: Incomplete | None = ...): ...
    # todo: resolve problem with update
    # def update(self, E: SupportsKeysAndGetItem[Any, Any], **F: Any) -> None: ...
    def update_extend(self, E: SupportsKeysAndItems[_KT, _VT], **F: Incomplete) -> None: ...
    def __setitem__(self, k: _KT, v: Incomplete) -> None: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __delitem__(self, k: _KT) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def pop(self, k: _KT, default: Incomplete = ...) -> Incomplete: ...
    def popall(self, k: _KT, default: Incomplete = ...) -> Iterable: ...
    def poplast(self, k=..., default=...): ...
    def iteritems(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def iterkeys(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def itervalues(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def todict(self, multi: bool = ...): ...
    def sorted(self, key: Incomplete | None = ..., reverse: bool = ...): ...
    def sortedvalues(self, key: Incomplete | None = ..., reverse: bool = ...): ...
    def inverted(self): ...
    def counts(self): ...
    def keys(self, multi: bool = ...): ...
    def values(self, multi: bool = ...): ...
    def items(self, multi: bool = ...): ...
    def __iter__(self): ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...
    def viewkeys(self): ...
    def viewvalues(self): ...
    def viewitems(self): ...
OMD = OrderedMultiDict
MultiDict = OrderedMultiDict

class FastIterOrderedMultiDict(OrderedMultiDict):
    def iteritems(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def iterkeys(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...

class OneToOne(dict):
    inv: Incomplete
    def __init__(self, *a, **kw) -> None: ...
    @classmethod
    def unique(cls, *a, **kw): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def setdefault(self, key, default: Incomplete | None = ...): ...
    # todo: resolve problem with update
    # def update(self, dict_or_iterable, **kw) -> None: ...

class ManyToMany:
    data: Incomplete
    inv: Incomplete
    def __init__(self, items: Incomplete | None = ...) -> None: ...
    def get(self, key, default=...): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, vals) -> None: ...
    def __delitem__(self, key) -> None: ...
    def update(self, iterable) -> None: ...
    def add(self, key, val) -> None: ...
    def remove(self, key, val) -> None: ...
    def replace(self, key, newkey) -> None: ...
    def iteritems(self) -> Generator[Incomplete, None, None]: ...
    def keys(self): ...
    def __contains__(self, key): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __eq__(self, other): ...

def subdict(d, keep: Incomplete | None = ..., drop: Incomplete | None = ...): ...

class FrozenHashError(TypeError): ...

class FrozenDict(dict):
    def updated(self, *a, **kw): ...
    @classmethod
    def fromkeys(cls, keys, value: Incomplete | None = ...): ...
    def __reduce_ex__(self, protocol): ...
    def __hash__(self): ...
    def __copy__(self): ...
    __ior__: Incomplete
    __setitem__: Incomplete
    __delitem__: Incomplete
    update: Incomplete
    setdefault: Incomplete
    pop: Incomplete
    popitem: Incomplete
    clear: Incomplete
