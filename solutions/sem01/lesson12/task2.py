from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    list_iter: list[Any] = []
    iterator = iter(iterable)
    try:
        while True:
            elem: Any = next(iterator)
            yield elem
            list_iter.append(elem)
    except StopIteration:
        if not list_iter:
            return
        i: int = 0
        while True:
            yield list_iter[i % len(list_iter)]
            i += 1
