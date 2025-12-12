from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    iterable_list = []
    for item in iterable:
        iterable_list.append(item)
        yield item
    if len(iterable_list) == 0:
        return None
    num = 0
    while True:
        yield iterable_list[num]
        num = (num + 1) % (len(iterable_list))
