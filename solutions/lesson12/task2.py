from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elem = []
    for it in iterable:
        elem.append(it)
        yield it

    if not elem:
        return

    i = 0
    n = len(elem)
    while True:
        yield elem[i]
        i = (i + 1) % n
