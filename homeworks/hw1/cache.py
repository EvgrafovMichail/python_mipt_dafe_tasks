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
    # ваш код
    try:
        capacity = round(capacity)
    except Exception:
        raise TypeError
    if capacity < 1:
        raise ValueError

    def decorator(func):
        cache = dict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items()))) if kwargs else args
            if key not in cache:
                result = func(*args, **kwargs)
                cache[key] = result
                if len(cache) > capacity:
                    first_key = next(iter(cache))
                    del cache[first_key]
                return result
            result = cache.pop(key)
            cache[key] = result
            return result

        return wrapper

    return decorator


@lru_cache(2)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(2)
def fib2(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
