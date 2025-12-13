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

    # ваш код
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if type(e) in exception_to_api_exception:
                    exception_type = exception_to_api_exception[type(e)]
                    if isinstance(exception_type, type):
                        raise exception_type() from None
                    else:
                        raise exception_type from None
                raise

        return wrapper

    return decorator
