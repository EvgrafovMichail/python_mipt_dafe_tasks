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
    def deco(func):
        def wrapper(*args, **kwargs):
            try:

                res = func(*args, **kwargs)
                return res

            except Exception as exception:

                if type(exception) in exception_to_api_exception.keys():
                    raise exception_to_api_exception[type(exception)]

                else:
                    raise exception

        return wrapper
    return deco

