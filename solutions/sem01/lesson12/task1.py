from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    it = iter(iterable)

    while True:
        lst = []
        while len(lst) < size:
            try:
                lst.append(next(it))
            except StopIteration:
                if lst:
                    yield tuple(lst)
                return

        if len(lst) == size:
            yield tuple(lst)
