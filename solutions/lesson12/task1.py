from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]: 
    chunk = []
    for i in iterable:
        chunk.append(i)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk = []
    if len(chunk) != 0:
        yield tuple(chunk)
        
