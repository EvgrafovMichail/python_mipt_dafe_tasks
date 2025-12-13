from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    if not iterable:
        return
    lst = []
    for elem in iterable:
        yield elem
        lst.append(elem)
    num = 0
    while True:
        yield lst[num % len(lst)]
        num += 1
