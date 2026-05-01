from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []

    for item in iterable:
        cache.append(item)
        yield item

    if not cache:
        return

    index = 0
    while True:
        yield cache[index]
        index = (index + 1) % len(cache)