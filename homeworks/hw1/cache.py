from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        capacity = round(capacity)
    except Exception:
        raise TypeError
    if capacity < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache_dictionary: dict[tuple, R] = {}

        def wrapper(*args: P.args, **kwargs: P.kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache_dictionary:
                result = cache_dictionary.pop(key)
                cache_dictionary[key] = result
                return result
            result = func(*args, **kwargs)
            cache_dictionary[key] = result
            if len(cache_dictionary) > capacity:
                cache_dictionary.pop(next(iter(cache_dictionary)))
            return result

        return wrapper

    return decorator
