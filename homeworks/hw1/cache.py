from functools import wraps
from collections import OrderedDict
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)


class func_args:
    args: tuple
    kwargs: tuple

    def __init__(self, args: tuple, kwargs: dict) -> None:
        self.args = args
        self.kwargs = tuple(sorted(kwargs.items()))

    def __eq__(self, other) -> bool:
        if not isinstance(other, func_args):
            return NotImplemented

        return (self.args, self.kwargs) == (other.args, other.kwargs)

    def __hash__(self) -> int:
        return hash((self.args, self.kwargs))


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
        capacity = int(round(capacity))
    except Exception:
        raise TypeError

    if capacity < 1:
        raise ValueError

    def add_cache(func: Callable[P, R]) -> Callable[P, R]:
        cache: OrderedDict = OrderedDict()

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            nonlocal cache
            key = func_args(args, kwargs)

            if key in cache:
                cache.move_to_end(key)
                return cache[key]

            else:
                result = func(*args, **kwargs)
                cache[key] = result

                if len(cache) > capacity:
                    cache.popitem(last=False)

                return result

        return wrapper

    return add_cache
