from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []
    for i in iterable:
        cache.append(i)
        yield i
    if not cache:
        return
    while True:
        for i in cache:
            yield i