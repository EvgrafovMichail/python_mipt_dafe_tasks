from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    # ваш код

    elements = []
    for element in iterable:
        yield element
        elements.append(element)

    if not elements:
        return

    size = len(elements)
    ind = 0

    while True:
        ind %= size
        yield elements[ind]
        ind += 1
