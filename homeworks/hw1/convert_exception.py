from functools import wraps
from typing import Callable, Dict, ParamSpec, Type, TypeVar, Union

P = ParamSpec("P")
R = TypeVar("R")

ExceptionMapping = Dict[Type[Exception], Union[Type[Exception], Exception]]


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: ExceptionMapping,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for exc_type, replacement in exception_to_api_exception.items():
                    if isinstance(e, exc_type):
                        if isinstance(replacement, type) and issubclass(
                            replacement, Exception
                        ):
                            raise replacement(str(e)) from e
                        else:
                            raise replacement from e
                raise

        return wrapper

    return decorator


class OriginalError(Exception):
    pass


class APIError(Exception):
    pass


exception_mapping: ExceptionMapping = {
    OriginalError: APIError,
    ValueError: RuntimeError("Invalid value provided"),
}


@convert_exceptions_to_api_compitable_ones(exception_mapping)
def example_function(x: int) -> int:
    if x < 0:
        raise OriginalError("Negative value")
    return x * 2


def main() -> None:
    try:
        example_function(-5)
    except APIError:
        pass


if __name__ == "__main__":
    main()