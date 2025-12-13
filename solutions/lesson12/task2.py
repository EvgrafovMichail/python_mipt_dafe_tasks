from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for item in iterable:
        elements.append(item)
        yield item

    if not elements:
        return

    index = 0
    while True:
        yield elements[index]
        index = (index + 1) % len(elements)
