from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int):
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
    def decorator(func):
        try:
            nonlocal capacity
            capacity = round(int(capacity))
            if (capacity < 1):
                raise ValueError
        except TypeError:
            raise TypeError
            
        cache = {}  # Обычный словарь
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items()))) if kwargs else args

            if key in cache:
                # Имитируем move_to_end: удаляем и добавляем заново
                value = cache[key]
                del cache[key]
                cache[key] = value
                return value

            result = func(*args, **kwargs)
            cache[key] = result

            if len(cache) > capacity:
                # Удаляем первый элемент (самый старый)
                first_key = next(iter(cache))
                del cache[first_key]

            return result

        return wrapper

    return decorator