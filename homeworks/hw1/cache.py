from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:

    try:
        capacity = int(capacity)
    except (ValueError, TypeError):
        raise TypeError("Capacity must be convertible to int")

    if capacity < 1:
        raise ValueError("Capacity must be >= 1")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        
        cache = {}
        
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            
            key = args
            
            if key in cache:
                result = cache.pop(key)
                cache[key] = result
                return result

            if len(cache) >= capacity:
                for old_key in cache:
                    cache.pop(old_key)
                    break
                    
            result = func(*args, **kwargs)
            cache[key] = result
            
            return result

        return wrapper
    return decorator