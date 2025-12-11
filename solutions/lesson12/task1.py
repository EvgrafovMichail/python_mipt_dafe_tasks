from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    if not iterable:
        return tuple()

    my_iter = iter(iterable)

    while True:
        result = []
        try:
            for _ in range(size):
                result.append(next(my_iter))
            yield tuple(result)
        except StopIteration:
            if result:
                yield tuple(result)
            break
