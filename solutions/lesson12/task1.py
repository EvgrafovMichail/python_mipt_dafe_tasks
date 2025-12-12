from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    if size <= 0:
        raise ValueError

    chunk = []

    for elem in iterable:
        chunk.append(elem)
        if len(chunk) >= size:
            yield tuple(chunk)
            chunk = []
    if chunk:
        yield tuple(chunk)
