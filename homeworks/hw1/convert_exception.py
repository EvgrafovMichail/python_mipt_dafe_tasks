from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")

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


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: dict[type[Exception], type[Exception] | Exception],
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exp:
                for exp_key, exp_value in exception_to_api_exception.items():
                    if isinstance(exp, exp_key):
                        raise exp_value from None

                raise

        return wrapper

    return decorator
