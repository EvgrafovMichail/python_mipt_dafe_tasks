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
    if not (isinstance(capacity, int) or isinstance(capacity, float)):
        raise TypeError("Capacity must be int(or float) and greater than 1")
    if not is_valid_args(capacity):
        raise ValueError("Capacity must be greater than 1")
    capacity = round(capacity)
    cache, times = {}, {}

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        def inner(*args: P.args) -> R:
            if (vals := hash(*args)) not in cache:
                res = func(*args)
                if len(cache) >= capacity:
                    least_time_used = 10**5
                    last_used = None
                    for key in times:
                        if times[key] < least_time_used:
                            least_time_used = times[key]
                            last_used = key
                    cache.pop(last_used)
                cache[vals], times[vals] = res, 0
            else:
                res = cache[vals]
                times[vals] += 1
            return res

        return inner

    return wrapper


def is_valid_args(capacity: int | float) -> bool:
    return round(capacity) > 1
