from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for elem in iterable:
        elements.append(elem)
        yield elem
    if not elements:
        return
    while True:
        for elem in elements:
            yield elem
