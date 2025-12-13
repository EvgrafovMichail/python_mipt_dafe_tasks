from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iterator = iter(iterable)
    while True:
        try:
            chunk = []
            for _ in range(size):
                chunk.append(next(iterator))
        except StopIteration:
            if chunk:
                yield tuple(chunk)
            break
        else:
            yield tuple(chunk)
            
#print(tuple(chunked([1, 2, 3, 4, 5], 2)))