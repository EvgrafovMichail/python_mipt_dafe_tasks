from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []

    for element in iterable:
        cache.append(element)
        yield element

    if cache == []:
        return None

    pos = 0
    while True:
        yield cache[pos]
        pos += 1
        if pos >= len(cache):
            pos = 0