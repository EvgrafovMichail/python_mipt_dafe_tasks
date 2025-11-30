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
    def trying(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                error = type(err)
                if error in exception_to_api_exception:
                    error_type = exception_to_api_exception[error]
                    if isinstance(error_type, type):
                        raise error_type() from None
                    else:
                        raise error_type from None
                else:
                    raise

        return wrapper

    return trying
