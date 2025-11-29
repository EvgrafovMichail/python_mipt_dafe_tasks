from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        cap = round(capacity)
    except Exception:
        raise TypeError
    if cap < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}
        order = []

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                order.remove(key)
                order.append(key)
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result
            order.append(key)

            if len(cache) > cap:
                del cache[order.pop(0)]

            return result

        return wrapper

    return decorator
