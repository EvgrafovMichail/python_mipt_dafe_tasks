from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []

    for elem in iterable:
        cache.append(elem)
        yield elem

    if not cache:
        return

    idx = 0
    while True:
        yield cache[idx]
        idx = (idx + 1) % len(cache)
