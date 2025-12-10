from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)

    while True:
        current_chunk = []
        for _ in range(size):
            try:
                current_chunk.append(next(iterator))
            except StopIteration:
                if current_chunk:
                    yield tuple(current_chunk)
                return
        yield tuple(current_chunk)
