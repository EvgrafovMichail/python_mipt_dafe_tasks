from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    iterator = iter(iterable)
    items = []
    # cache=list(iterable)
    while True:
        try:
            item = next(iterator)
            items.append(item)
            yield item
        except StopIteration:
            break
    if not items:
        return
    iterator = iter(items)
    while True:
        try:
            yield next(iterator)
        except StopIteration:
            iterator = iter(items)
