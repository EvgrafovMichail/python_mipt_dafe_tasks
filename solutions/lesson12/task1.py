from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    if not iterable:
        return tuple()

    iterator = iter(iterable)

    while True:
        out = []
        try:
            for _ in range(size):
                out.append(next(iterator))
            yield tuple(out)
        except StopIteration:
            if out:
                yield tuple(out)
            break
