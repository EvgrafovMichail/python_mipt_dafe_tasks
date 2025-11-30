import functools
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
    def handle_error(func):
        
        @functools.wraps(func)
        def wraps(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if type(e) in exception_to_api_exception:
                    api_exception = exception_to_api_exception[type(e)]
                    raise api_exception from None
                raise

        return wraps

    return handle_error
