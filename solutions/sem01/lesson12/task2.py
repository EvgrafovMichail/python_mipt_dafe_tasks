from typing import Iterable, Generator, Any


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    lst = []
    iterator = iter(iterable)
    collecting = True

    while True:
        if collecting:
            try:
                item = next(iterator)
                lst.append(item)
                yield item
            except StopIteration:
                collecting = False

        if not collecting:
            if not lst:
                return
            for item in lst:
                yield item
