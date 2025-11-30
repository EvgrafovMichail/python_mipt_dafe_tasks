from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if not isinstance(capacity, int) or capacity < 1:
        raise ValueError("capacity must be positive integer")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache_values = {}
        cache_keys = []

        def create_key_part(arg):
            if isinstance(arg, (int, float)):
                try:
                    if round(arg) == arg:
                        return round(arg)
                    return arg
                except (TypeError, ValueError) as e:
                    raise TypeError(f"Несовместимый аргумент: {arg}") from e
            
            try:
                hash(arg)
                return arg
            except TypeError as e:
                raise TypeError(f"Несовместимый аргумент: {arg}") from e

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            
            processed_args = tuple(create_key_part(arg) for arg in args)
            
            processed_kwargs = tuple(
                (k, create_key_part(v)) for k, v in sorted(kwargs.items())
            )
            
            key = (processed_args, processed_kwargs)

            if key in cache_values:
                cache_keys.remove(key)
                cache_keys.append(key)
                return cache_values[key]

            if len(cache_keys) >= capacity:
                old_key = cache_keys.pop(0)
                del cache_values[old_key]

            result = func(*args, **kwargs)
            
            cache_keys.append(key)
            cache_values[key] = result
            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        return wrapper

    return decorator