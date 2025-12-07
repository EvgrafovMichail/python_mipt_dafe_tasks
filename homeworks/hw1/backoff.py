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

def convert_exception(
    from_exception: Union[Type[Exception], Tuple[Type[Exception], ...]],
    to_exception: Type[Exception],
    message: str = "An error occurred"
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except from_exception as e:
                raise to_exception(message) from e
        return wrapper
    return decorator

class OriginalError(Exception):
    pass

class NewError(Exception):
    pass

@convert_exception(OriginalError, NewError, "Converted error")
def risky_function(x: int) -> int:
    if x < 0:
        raise OriginalError("Negative value")
    return x * 2

def main() -> None:
    try:
        result = risky_function(-5)
    except NewError:
        result = 0

if __name__ == "__main__":
    main()