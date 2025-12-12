from typing import Any, Generator, Iterable


def infinite_generator():
    i = 1
    while True:
        yield i
        i += 1


def finite_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    if not iterable:
        return
    el = []
    for x in iterable:
        el.append(x)
        print(x, el)
        yield x
    while True:
        for item in el:
            yield item
