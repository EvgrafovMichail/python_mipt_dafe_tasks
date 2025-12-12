from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    item_list = []
    for item in iterable:
        item_list.append(item)
        yield item

    if not item_list:
        return

    ind = 0
    while True:
        yield item_list[ind]
        ind = (ind + 1) % len(item_list)
