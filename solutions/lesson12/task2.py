from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    it = list(iterable)
    n = len(it)

    if not it:
        return

    i = 0
    while True:
        yield it[i]
        i = (i + 1) % n
