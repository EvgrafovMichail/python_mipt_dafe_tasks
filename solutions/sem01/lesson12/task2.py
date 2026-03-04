from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
            cache.append(item)
            yield item
        except StopIteration:
            break

    if not cache:
        return

    index = 0
    while True:
        yield cache[index]
        index = (index + 1) % len(cache)
