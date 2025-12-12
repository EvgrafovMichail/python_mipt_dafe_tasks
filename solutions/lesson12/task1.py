from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    rez = tuple()
    i = 0
    for el in iter(iterable):
        if i % size == 0 and i != 0:
            yield rez
            rez = ()
            rez += (el,)
        else:
            rez += (el,)
        i += 1
    if rez:
        yield rez
