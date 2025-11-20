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
        capacity = round(capacity)
    except TypeError:
        raise TypeError(f"{type(capacity).__name__} неверный тип для размера кэша") from None
    if capacity < 1:
        raise ValueError

    cache = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_args = args + tuple(sorted(kwargs.items()))
            if func_args in cache:
                cache[func_args][1] = 0
                return cache[func_args][0]
            else:
                for k in cache.keys():
                    cache[k][1] += 1

                if len(cache) == capacity:
                    least_used_key = sorted(cache.items(), key=lambda x: x[1][1])[-1][0]
                    cache.pop(least_used_key)
                res = func(*args, **kwargs)
                cache[func_args] = [res, 0]
                return res

        return wrapper

    return decorator
