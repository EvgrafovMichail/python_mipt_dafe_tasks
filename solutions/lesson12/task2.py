from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    # ваш код
    saved = []

    for element in iterable:
        yield element
        saved.append(element)
    if not saved:
        return
    while True:
        yield from saved
