from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    chunk = []
    for i in iterable:
        if len(chunk) < size:
            chunk.append(i)
        else:
            yield tuple(chunk)
            chunk = [i]
    if len(chunk) != 0:
        yield tuple(chunk)
