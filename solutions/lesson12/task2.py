from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    def generator():
        cache = list()

        try:
            it = iter(iterable)
            first_item = next(it)
            cache.append(first_item)

        except StopIteration:
            return

        yield first_item

        while True:
            try:
                temp = next(it)
                cache.append(temp)
                yield temp

            except StopIteration:
                for i in cache:
                    yield i

    return generator()
