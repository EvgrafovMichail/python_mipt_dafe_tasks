from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    allelem = []
    for elem in iterable:
        allelem.append(elem)
        yield elem

    if not allelem:
        return

    while True:
        for elem in allelem:
            yield elem
