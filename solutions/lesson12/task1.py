from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    buffer = []

    for elem in iterable:
        buffer.append(elem)

        if len(buffer) == size:
            yield tuple(buffer)
            buffer.clear()

    if buffer:
        yield tuple(buffer)
