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
        int_capacity = round(capacity)
    except TypeError:
        raise TypeError
    if int_capacity < 1:
        raise ValueError

    def decorator(func):
        lru_dict = {}

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # nonlocal lru_dict
            if kwargs:
                current_key = (args, tuple(sorted(kwargs.items())))
            else:
                current_key = args

            if current_key in lru_dict:
                result = lru_dict.pop(current_key)
                lru_dict[current_key] = result
                return result

            if len(lru_dict) >= int_capacity:
                first_key = next(iter(lru_dict))
                lru_dict.pop(first_key)

            result = func(*args, **kwargs)
            lru_dict[current_key] = result
            return result

        return wrapper

    return decorator
