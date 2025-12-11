from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    items = []
    for item in iterable:
        items.append(item)
        yield item

    if not items:
        return

    index = 0
    length = len(items)
    while True:
        yield items[index]
        index = (index + 1) % length
