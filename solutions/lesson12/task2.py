from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for elem in iterable:
        yield elem
        elements.append(elem)

    if not elements:
        return

    size = len(elements)
    index = 0
    while True:
        index %= size
        yield elements[index]
        index += 1
