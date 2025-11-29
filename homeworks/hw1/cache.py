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

    def decorator(func):
        storage = {}

        def wrapper(*args, **kwargs):
            kw = tuple(kwargs.items())
            packed = (args, kw)

            exist = storage.get(packed)
            if exist is not None:
                storage.pop(packed)
                storage[packed] = exist
                return exist
            else:
                ans = func(*args, **kwargs)
                storage[packed] = ans

            if len(storage) > capacity:
                old_key = list(storage.keys())[0]
                storage.pop(old_key)

            return ans

        return wrapper

    return decorator
