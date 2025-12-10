from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    copy = []
    flag = True
    iterator = iter(iterable)
    while True:
        while flag:
            try:
                elem = next(iterator)
                copy.append(elem)
                yield elem
            except StopIteration:
                flag = False
                break
        if not copy:
            break
        for elem in copy:
            yield elem
