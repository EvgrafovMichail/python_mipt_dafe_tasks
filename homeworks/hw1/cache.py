from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        capacity = round(capacity)
    except (TypeError, ValueError):
        raise TypeError("Capacity must be a roundable value")

    if capacity < 1:
        raise ValueError("Capacity must be at least 1")

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}

        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            func_code = func.__code__
            arg_names = func_code.co_varnames[: func_code.co_argcount]
            if not (defaults := func.__defaults__):
                defaults = ()
            num_non_defaults = func_code.co_argcount - len(defaults)

            key = []
            for i, arg_name in enumerate(arg_names):
                if i < len(args):
                    key.append(args[i])
                elif arg_name in kwargs:
                    key.append(kwargs[arg_name])
                else:
                    key.append(defaults[i - num_non_defaults])
            key = tuple(key)

            if key in cache:
                cache[key] = (result := cache.pop(key))
                return result
            else:
                if len(cache) > capacity - 1:
                    del cache[next(iter(cache))]
                cache[key] = (result := func(*args, **kwargs))
                return result

        return inner

    return wrapper
