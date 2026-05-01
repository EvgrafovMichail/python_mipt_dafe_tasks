from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    i = 0
    while True:
        try:
            chunk = []
            for _ in range(size):
                chunk.append(next(iterator))
            i += size
            yield tuple(chunk)
        except StopIteration:
            if chunk:
                yield tuple(chunk)
            break
