from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    count = 1
    cache = []
    while True:
        if count > 1 and cache == []:
            return None

        if count == 1:
            obj = iterable
        else:
            obj = cache
        for i in obj:
            if count == 1:
                cache.append(i)
            yield i
        count += 1


circle_gen = circle((i for i in range(3)))

for i in range(5):
    print(next(circle_gen))
