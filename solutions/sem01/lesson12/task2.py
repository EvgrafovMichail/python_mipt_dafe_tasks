from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elems = []
    for i in iterable:
        yield i
        elems.append(i)

    if not elems:
        return

    while True:
        for i in elems:
            yield i
