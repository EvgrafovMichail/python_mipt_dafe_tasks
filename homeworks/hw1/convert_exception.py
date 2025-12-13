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

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            excepted_errors = tuple(exception_to_api_exception.keys())

            try:
                return function(*args, **kwargs)

            except excepted_errors as exc:
                for pyexc, apiexc in exception_to_api_exception.items():
                    if isinstance(exc, pyexc):
                        raise apiexc from None

        return wrapper

    return decorator
