from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []

    for i in iter(iterable):
        elements.append(i)
        yield i

    if not elements:
        return None

    while elements:
        for i in elements:
            yield i
