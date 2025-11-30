from functools import wraps
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)
P = ParamSpec("P")
R = TypeVar("R")
def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: dict[type[Exception], type[Exception] | Exception],
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                exc_type = type(exc)
                new_exc = exception_to_api_exception.get(exc_type)
                if new_exc:
                    raise new_exc from None
                raise exc from None

            return result

        return wrapper

    return decorator
