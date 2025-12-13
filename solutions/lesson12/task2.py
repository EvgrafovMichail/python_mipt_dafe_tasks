from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for element in iterable:
        elements.append(element)
        yield element
    while True:
        for element in elements:
            yield element    