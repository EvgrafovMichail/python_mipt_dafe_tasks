from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    Any 
)
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: dict[type[Exception], type[Exception] | Exception],
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator (func : Callable) -> Callable:
        @wraps(func)
        def wrapper (*args, **kwargs) -> Any:
            try :
                return func(*args, **kwargs)
            except Exception as error:
                for old_error_type, api_error in exception_to_api_exception.items():
                    if isinstance(error, old_error_type):
                 #нашли перевод 
                        if isinstance(api_error, type) and issubclass(api_error, Exception):
                            raise api_error(str(error)) from error
                        else:
                            raise api_error from error
                raise error 
        return wrapper
    return decorator
