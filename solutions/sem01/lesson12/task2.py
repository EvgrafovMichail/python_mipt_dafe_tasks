from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    iterator = iter(iterable)
    cache = []
    i = 0
    while True:
        if i < len(cache):
            yield cache[i]

        else:
            try:
                elem = next(iterator)
                cache.append(elem)
                yield cache[i]

            except StopIteration:
                try:
                    yield cache[i % len(cache)]

                except ZeroDivisionError:
                    return 0
        i += 1
