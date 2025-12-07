from functools import wraps
from typing import (
    Callable,
    Dict,
    ParamSpec,
    Tuple,
    Type,
    TypeVar,
    Union,
)

P = ParamSpec("P")
R = TypeVar("R")

ExceptionMapping = Dict[Type[Exception], Union[Type[Exception], Exception]]


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: ExceptionMapping,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
        
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            raise NotImplementedError

        return wrapper
        
    return decorator