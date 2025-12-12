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
        capacity_int = round(capacity)
    except (TypeError, ValueError) as e:
        raise TypeError(f"capacity must be roundable object, got {type(capacity).__name__}") from e
    
    if capacity_int < 1:
        raise ValueError(f"capacity must be at least 1, got {capacity_int}")
    
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}
        
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                result = cache.pop(key)
                cache[key] = result
                return result
            
            result = func(*args, **kwargs)
            
            cache[key] = result
            
            if len(cache) > capacity_int:
                oldest_key = next(iter(cache))
                del cache[oldest_key]
            
            return result
        
        return wrapper
    
    return decorator
