from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    cur_block = []
    for elem in iterable:
        cur_block.append(elem)
        if len(cur_block) == size:
            yield tuple(cur_block)
            cur_block = []
    if cur_block:
        yield tuple(cur_block)
