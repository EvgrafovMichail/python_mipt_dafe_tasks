from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    block = []
    for element in iterable:
        block.append(element)

        while len(block) == size:
            yield tuple(block)
            block = []
            break

    while block:
        yield tuple(block)
        break
