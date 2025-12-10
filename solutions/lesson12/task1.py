from typing import Any, Generator, Iterable

def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    k = 0
    chunk = []
    while True:
        if k < size:
            try:
                element = next(iterator)
                chunk.append(element)
            except StopIteration:
                break
        else:
            yield tuple(chunk)
            chunk = []
            try:
                element = next(iterator)
                chunk.append(element)
            except StopIteration:
                break
            k = 0
        k += 1
    if chunk:
        yield tuple(chunk)