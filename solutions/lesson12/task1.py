from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    chunk: list[Any] = []
    iterator = iter(iterable)
    try:
        while True:
            elem: Any = next(iterator)
            chunk.append(elem)
            if len(chunk) == size:
                yield tuple(chunk)
                chunk.clear()

    except StopIteration:
        if len(chunk) != 0:
            yield tuple(chunk)
