from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    if size < 1:
        raise ValueError()

    iterator = iter(iterable)

    while True:
        chunk = []
        try:
            for i in range(size):
                element = next(iterator)
                chunk.append(element)

        except StopIteration:
            pass

        if chunk:
            yield tuple(chunk)

        if len(chunk) < size:
            return
