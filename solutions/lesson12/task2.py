from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    buffer = []
    it = iter(iterable)
    collecting = True

    while True:
        if collecting:
            try:
                value = next(it)
                buffer.append(value)
                yield value
                continue
            except StopIteration:
                collecting = False

        if not buffer:
            return

        for value in buffer:
            yield value