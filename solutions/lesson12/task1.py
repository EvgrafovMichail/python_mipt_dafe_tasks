
from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:

    iterator = iter(iterable)
    
    while True:
        chunk = []
        try:
            for i in range(size):
                chunk.append(next(iterator))
        except StopIteration:
            if chunk:
                yield tuple(chunk)
            break
        
        yield tuple(chunk)
