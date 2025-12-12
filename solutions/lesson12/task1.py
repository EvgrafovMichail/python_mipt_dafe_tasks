from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    # ваш код
    iterator = iter(iterable)
    while True:
        chunk = []
        for i in range(size):
            try:
                element = next(iterator)
                chunk.append(element)
            except StopIteration:
                if len(chunk) > 0:
                    yield tuple(chunk)
                return
        yield tuple(chunk)
