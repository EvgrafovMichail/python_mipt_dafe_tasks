from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    cache = []

    for element in iterable:
        yield element
        cache.append(element)

    if not cache:
        return

    while True:
        for element in cache:
            yield element


circle_gen = circle("abc")

for i in range(5):
    print(next(circle_gen))
# a
# b
# c
# a
# b
