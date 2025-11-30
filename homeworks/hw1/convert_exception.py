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
    """
    Параметризованный декоратор для замены внутренних исключений на API-исключении.

    Args:
        exception_to_api_exception: словарь:
            ключи - внутренние исключения, которые надо заменить,
            значения - API-исключения, которые надо возбудить
                вместо внутренних исключений

    Returns:
        Декоратор для непосредственного использования.
    """

    def decorator_replacement_exclusive(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                caught_exception_type = type(e)

                for exception_pair in exception_to_api_exception.items():
                    internal_exc_type = exception_pair[0]
                    api_exc = exception_pair[1]

                    if caught_exception_type == internal_exc_type:
                        if type(api_exc) is type:
                            raise api_exc() from None
                        else:
                            raise api_exc from None

                raise

        return wrapper

    return decorator_replacement_exclusive
