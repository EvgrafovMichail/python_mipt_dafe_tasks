from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    chunk = []
    for elem in iterable:
        chunk.append(elem)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk = []
    if chunk:
        yield tuple(chunk)
