from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    data = []
    for item in iterable:
        yield item
        data.append(item)

    if not data:
        return

    while True:
        for item in data:
            yield item
