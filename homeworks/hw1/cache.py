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

    except Exception:
        raise TypeError

    if capacity < 1:
        raise ValueError

    def decorator(func: R) -> R:
        used = {}

        @wraps(func)
        def wrapper(*args: ..., **kwargs: ...) -> R:
            if args in used:
                result = used[args]
                del used[args]
                used[args] = result
                return result

            result = func(*args, **kwargs)
            used[args] = result

            if len(used) > capacity:
                oldest_key = list(used.keys())[0]
                del used[oldest_key]

            return result

        return wrapper

    return decorator
