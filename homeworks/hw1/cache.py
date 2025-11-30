from functools import wraps
from typing import Callable, ParamSpec, TypeVar
P = ParamSpec("P")
R = TypeVar("R")
def lru_cache(capacity: int | float) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if not (isinstance(capacity, int) or isinstance(capacity, float)):
        raise TypeError("input error")
    capacity = round(capacity)
    if not capacity > 1:
        raise ValueError("input error")
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}
        order = []
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if kwargs:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args
            if key in cache:
                result = cache[key]
                order.remove(key)
                order.append(key)
                return result
            if len(cache) >= capacity:
                lru_key = order.pop(0)
                del cache[lru_key]
            result = func(*args, **kwargs)
            cache[key] = result
            order.append(key)
            return result
        return wrapper
    return decorator