from collections import OrderedDict
from typing import Callable, ParamSpec, TypeVar

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
        capacity_int = round(capacity)
    except TypeError:
        raise TypeError("Exception occurred while trying to round capacity")

    if capacity_int < 1:
        raise ValueError("Capacity must be more or equal 1")

    # Самые недавно используемые элементы в конце,давно используемые - в начале
    cache = OrderedDict()

    def decorator(func: Callable[[P], R]) -> Callable[[P], R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            args_list = args + tuple(sorted([(k, v) for k, v in kwargs.items()]))
            if args_list in cache:
                result = cache[args_list] = cache.pop(args_list)
                return result

            result = func(*args, **kwargs)
            cache[args_list] = result

            if len(cache) > capacity_int:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator
