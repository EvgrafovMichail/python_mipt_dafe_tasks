from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    it = iter(iterable)

    while True:
        chunk = ()

        try:
            for _ in range(size):
                chunk += (next(it),)

        except StopIteration:
            if chunk:
                yield tuple(chunk)
            break
        else:
            yield tuple(chunk)
