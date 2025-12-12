from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cashe = []
    for item in iterable:
        cashe.append(item)
        yield item
    if cashe:
        while True:
            for item in cashe:
                yield item
