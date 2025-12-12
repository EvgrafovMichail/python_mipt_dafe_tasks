from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    iter_var = iter(iterable)
    res = []
    for item in iter_var:
        res.append(item)
        if len(res) == size:
            yield tuple(res)
            res = []
    if res:
        yield tuple(res)
