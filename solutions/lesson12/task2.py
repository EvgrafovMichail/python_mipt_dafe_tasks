from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    # ваш код
    cache = []
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            cache.append(item)
            yield item
        except StopIteration:
            break
    if cache:
        index = 0
        while True:
            yield cache[index]
            index = (index + 1) % len(cache)
