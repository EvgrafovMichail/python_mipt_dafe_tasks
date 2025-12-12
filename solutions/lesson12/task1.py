from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    while True:
        chunk = []
        try:
            for elem in range(size):
                chunk.append(next(iterator))
            yield tuple(chunk)
        except StopIteration:
            if chunk:
                yield tuple(chunk)
            break
