from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []

    for el in iterable:
        yield el
        cache.append(el)

    i = 0
    while cache:
        yield cache[i]
        i += 1

        if i == len(cache):
            i = 0
            continue
