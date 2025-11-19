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

    def decorator(func):
        cache = dict()

        def wraps(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items()))) if kwargs else args
            if key in cache:
                result = cache.pop(key)
                cache[key] = result
                return result

            if len(cache) >= capacity:
                first_key = next(iter(cache))
                cache.pop(first_key)

            result = func(*args, **kwargs)
            cache[key] = result
            return result

        return wraps

    return decorator
