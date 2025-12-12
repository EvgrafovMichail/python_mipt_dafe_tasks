from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterable = iter(iterable)
    while True:
        chunk = []
        try:
            for i in range(size):
                chunk.append(next(iterable))
        except StopIteration:
            if chunk:
                yield tuple(chunk)
            return
        yield tuple(chunk)
