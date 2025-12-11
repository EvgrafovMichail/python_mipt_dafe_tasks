from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    collect = []
    try:
        while True:
            for _ in range(size):
                collect.append(next(iterator))
            yield tuple(collect)
            collect.clear()
    except StopIteration:
        if collect:
            yield tuple(collect)
