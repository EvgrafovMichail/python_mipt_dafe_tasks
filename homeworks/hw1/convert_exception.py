from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)
from functools import wraps

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

    def convert_error(error: Exception) -> Exception | None:
        for except_type, except_api in exception_to_api_exception.items():
            if isinstance(error, except_type):
                return except_api() if isinstance(except_api, type) else except_api
        return None

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                api_exception = convert_error(error)
                if api_exception is not None:
                    raise api_exception from None
                raise

        return wrapper

    return decorator
