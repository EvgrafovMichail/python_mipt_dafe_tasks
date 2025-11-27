from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

from unittest.mock import MagicMock, patch, Mock

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
        int_capacity: int = int(round(capacity))

    except Exception:
        raise TypeError

    else:
        if int_capacity < 1:
            raise ValueError
        
        def decorator(func: Callable[P, R]) -> Callable[P, R]:
            
            lru_dict: dict[tuple[object], object] = {}
            
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

                if args not in lru_dict.keys():
                    lru_dict[args] = func(*args, **kwargs)
                    if len(lru_dict) > int_capacity:
                        lru_dict.pop(next(iter(lru_dict)), None)
                
                else:
                    val = lru_dict[args]
                    lru_dict.pop(args, None)
                    lru_dict[args] = val

                return lru_dict[args]
            
            return wrapper
        
        return decorator