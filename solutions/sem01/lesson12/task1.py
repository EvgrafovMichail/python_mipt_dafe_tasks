from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    arr = []
    arr_size = 0
    for i in iterable:
        arr.append(i)
        arr_size += 1
        if arr_size == size:
            yield tuple(arr)
            arr = []
            arr_size = 0
    if arr:
        yield tuple(arr)
