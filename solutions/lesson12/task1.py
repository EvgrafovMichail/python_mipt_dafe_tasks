from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    res = []
    for i in iterable:
        res.append(i)
        if len(res) == size:
            yield tuple(res)
            res = []
    
    if res: 
        yield tuple(res)