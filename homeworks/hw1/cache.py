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
        raise
    if capacity < 1:
        raise ValueError

    def decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                value = cache.pop(key)  # Удаляем из текущей позиции
                cache[key] = value  # Добавляем в конец (самый новый)
                return value

            # Вычисляем функцию если ключа нет в кеше
            result = func(*args, **kwargs)
            cache[key] = result  # Добавляем результат в кеш

            # Если кеш переполнен - удаляем самый старый элемент (первый в словаре)
            if len(cache) > capacity:

                cache.pop(list(cache.keys())[0])

            return result

        return wrapper

    return decorator
