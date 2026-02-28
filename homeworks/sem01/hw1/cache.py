from functools import wraps
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
        max_size = round(capacity)
    except TypeError:
        raise TypeError
    if max_size < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = dict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                val = cache[key]
                del cache[key]
                cache[key] = val
                return cache[key]

            res = func(*args, **kwargs)
            cache[key] = res

            if len(cache) > max_size:
                first_key = next(iter(cache))
                del cache[first_key]

            return res

        return wrapper

    return decorator
