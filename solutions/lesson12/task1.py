from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    
    while True:
        part = []
        try:
            for i in range(size):
                part.append(next(iterator))
            yield tuple(part)
        except StopIteration:
            if part:
                yield tuple(part)
            return None