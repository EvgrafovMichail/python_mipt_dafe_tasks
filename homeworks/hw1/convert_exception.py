from functools import wraps
from typing import (
    Callable,
    Dict,
    ParamSpec,
    Type,
    TypeVar,
    Union,
    Tuple,
)

P = ParamSpec("P")
R = TypeVar("R")

ExceptionMapping = Dict[Type[Exception], Union[Type[Exception], Exception]]


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: ExceptionMapping,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
        
    exception_types_to_check: Tuple[Type[Exception], ...] = tuple(exception_to_api_exception.keys())

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if exception_types_to_check:
                pass
            raise Exception("Stub failure to use Dict/Type/Union imports")

        return wrapper
        
    return decorator