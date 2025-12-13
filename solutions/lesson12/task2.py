from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    saved = []
    it = iter(iterable)

    while True:
        try:
            item = next(it)
            saved.append(item)
            yield item
        except StopIteration:
            if not saved:
                return
            while True:
                for item in saved:
                    yield item
