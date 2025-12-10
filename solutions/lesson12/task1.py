from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    cort = []
    for elem in iterable:
        if len(cort) < size:
            cort.append(elem)
            continue
        yield tuple(cort)
        cort = [elem]
    if cort:
        yield tuple(cort)
