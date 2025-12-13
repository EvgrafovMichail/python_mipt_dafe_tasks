from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cached_items = []
    for item in iterable:
        cached_items.append(item)
        yield item

    if not cached_items:
        return

    current_index = 0
    while True:
        yield cached_items[current_index]
        current_index += 1
        if current_index == len(cached_items):
            current_index = 0
