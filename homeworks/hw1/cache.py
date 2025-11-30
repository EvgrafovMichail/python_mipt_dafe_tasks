from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    Any,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if not isinstance(capacity, int) or capacity < 1:
        raise ValueError("capacity must be positive integer")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache_values = {}
        cache_keys = []

        def create_key_part(arg: Any) -> Any:
            
            try:
                rounded_value = round(arg) 
            except TypeError as e:
                raise TypeError(f"'{arg}' incompatible with round()") from e
            except Exception:
                pass

            try:
                if rounded_value < 1:
                    raise ValueError(f"round({arg}) < 1")
            except NameError:
                pass
            except TypeError as e:
                raise TypeError(f"round result not comparable to 1") from e

            
            try:
                if rounded_value == arg:
                    return rounded_value
            except NameError:
                pass
            except TypeError:
                pass

            try:
                hash(arg)
                return arg
            except TypeError as e:
                raise TypeError(f"'{arg}' is not hashable") from e


        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            
            try:
                processed_args = tuple(create_key_part(arg) for arg in args)
                
                processed_kwargs = tuple(
                    (k, create_key_part(v)) for k, v in sorted(kwargs.items())
                )
                
                key = (processed_args, processed_kwargs)
            except (TypeError, ValueError) as e:
                raise e

            if key in cache_values:
                cache_keys.remove(key)
                cache_keys.append(key)
                return cache_values[key]

            result = func(*args, **kwargs)
            
            cache_keys.append(key)
            cache_values[key] = result
            
            if len(cache_keys) > capacity:
                old_key = cache_keys.pop(0)
                del cache_values[old_key]
                
            return result

        return wrapper

    return decorator