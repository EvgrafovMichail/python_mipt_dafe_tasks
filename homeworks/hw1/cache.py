from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    Args:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """

    try:
        capacity = round(capacity)
    except TypeError:
        raise TypeError()
    if capacity < 1:
        raise ValueError()

    def deco(func):
        cache = {}

        def wrapper(*args, **kwargs):
            nonlocal cache
            args = tuple(args)

            if args in cache.keys():
                item = cache[args]
                del cache[args]
                cache[args] = item
                return cache[args]

            else:
                if len(cache) == capacity:
                    del cache[next(iter(cache))]
                cache[args] = func(*args, **kwargs)
                return cache[args]

        return wrapper

    return deco

