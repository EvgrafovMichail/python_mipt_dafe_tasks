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

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: ..., **kwargs: ...) -> R:
            try:
                return func(*args, **kwargs)

            except Exception as exc:
                exc_type = exception_to_api_exception.get(type(exc))

                if exc_type:
                    if isinstance(exc_type, type):
                        raise exc_type() from None

                    else:
                        raise exc_type from None

                raise

        return wrapper

    return decorator
