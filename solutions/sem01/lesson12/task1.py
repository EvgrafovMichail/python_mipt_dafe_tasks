from typing import Any, Generator, Iterable


def chunked(iterable: Iterable[Any], size: int) -> Generator[tuple[Any, ...], None, None]:
    iterator = iter(iterable)

    while True:
        chunk = []

        for _ in range(size):
            try:
                element = next(iterator)
                chunk.append(element)
            except StopIteration:
                break

        if chunk:
            yield tuple(chunk)
        else:
            break
