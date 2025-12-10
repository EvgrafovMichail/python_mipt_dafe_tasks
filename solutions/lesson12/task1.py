from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    it = iter(iterable)

    while True:
        try:
            part = []
            for _ in range(size):
                part.append(next(it))
        except StopIteration:
            if part:
                yield tuple(part)
            return
        yield tuple(part)
