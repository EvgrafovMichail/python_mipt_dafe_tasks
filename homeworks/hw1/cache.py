from collections import OrderedDict
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

    def decorator(func: Callable) -> Callable:
        cashe = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kargs):
            key = (args, tuple(sorted(kargs.items())))
            if key in cashe:
                cashe.move_to_end(key)
                return cashe[key]
            res = func(*args, **kargs)
            cashe[key] = res
            cashe.move_to_end(key)
            if len(cashe) > capacity:
                cashe.popitem(last=False)
            return res

        return wrapper

    return decorator
