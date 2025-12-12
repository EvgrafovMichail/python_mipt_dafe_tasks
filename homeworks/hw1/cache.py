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
        cache_size = round(capacity)
    except (TypeError):
        raise TypeError("Размер кеша должен быть числом")
    if cache_size < 1:
        raise ValueError("Размер кеша должен быть положительным числом")

    def deco(func):
        cache = {}

        def wrapper(*args, **kwargs):
            named_args = tuple(sorted(kwargs.items())) if kwargs else ()
            key = (args, named_args)
            
            if key in cache:
                value = cache.pop(key)
                cache[key] = value
                return value
            
            result = func(*args, **kwargs)
            cache[key] = result
            
            if len(cache) > cache_size:
                all_keys = list(cache.keys())  
                oldest_key = all_keys[0]   
                del cache[oldest_key]
            
            return result
        
        return wrapper
    
    return deco