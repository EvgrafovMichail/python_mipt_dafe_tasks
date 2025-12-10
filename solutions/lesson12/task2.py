from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for i in iterable:
        elements.append(i)
        yield i
    while True:
        for i in elements:
            yield i