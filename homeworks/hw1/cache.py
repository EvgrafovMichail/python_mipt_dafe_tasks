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
        cap = round(capacity)
    except Exception:
        raise TypeError("capacity must be round-able")

    if cap < 1:
        raise ValueError("capacity must be >= 1")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                value = cache.pop(key)
                cache[key] = value
                return value

            if len(cache) == cap:
                cache.pop(list(cache.keys())[0])

            result = func(*args, **kwargs)
            cache[key] = result
            return result

        return wrapper

    return decorator

    # ваш код
