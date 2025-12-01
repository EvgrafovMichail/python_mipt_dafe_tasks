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
    size = round(capacity)
    if size < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            if cache.get(key):
                ret_val = cache[key]
                del cache[key]
                cache[key] = ret_val
                return ret_val

            result = func(*args, **kwargs)

            if len(cache) >= size:
                del cache[next(iter(cache))]

            cache[key] = result

            return result

        return wrapper

    return decorator
