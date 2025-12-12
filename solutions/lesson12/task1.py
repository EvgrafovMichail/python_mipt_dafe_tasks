from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    lst = []
    for i in iterable:
        lst.append(i)
        if len(lst) == size:
            yield tuple(lst)
            lst = []
    if lst:
        yield tuple(lst)


print(tuple(chunked("str", 4)))
