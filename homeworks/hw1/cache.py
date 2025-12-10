from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    Any
)

def create_cach(max_size):
    data = {} 
    order = []

    def get_from_cache(key):
        if key in data:
            order.remove(key)
            order.append(key)
            return data[key]
        return None
    
    def save_to_cache(key, value):
        if key in data:
            data[key] = value
            order.remove(key)
            order.append(key)
        else:
            if len(data) >= max_size:
                del data[order.pop(0)]
            data[key] = value 
            order.append(key)
    return get_from_cache, save_to_cache

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        valid_capacity = round(capacity)
    except:
        raise TypeError(f"{capacity} should be rounded")
    if valid_capacity <1:
        raise ValueError(f"{capacity} should be smaller then 1")
    
    def decorator(func: Callable[P, R])-> Callable[P, R]:
        data ={}
        order = []
        def wrapper (*args, **kwargs) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            if key in data:
                order.remove(key)
                order.append(key)
                return data[key]
            else:
                result = func(*args, **kwargs)

            if len(data) >= valid_capacity:
                del data[order.pop(0)]

            data[key] = result 
            order.append(key)
            return result
        return wrapper
    return decorator
            
