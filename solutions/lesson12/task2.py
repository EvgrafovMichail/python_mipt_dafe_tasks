from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    iterator = iter(iterable)
    cache = []
    index = 0
    while True:
        try:
            value = next(iterator)
            cache.append(value)
            yield value
        except StopIteration:
            if not cache:
                return
            break
    n = len(cache)
    while True:
        yield cache[index % n]
        index += 1
