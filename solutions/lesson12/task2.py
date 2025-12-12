from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    lst = []
    for i in iterable:
        lst.append(i)
        yield i
    if not lst:
        return
    while 1:
        for i in lst:
            yield i
