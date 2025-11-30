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
    def decorator(func: Callable):
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exept:
                ex_type = type(exept)

                if ex_type in exception_to_api_exception:
                    replacement = exception_to_api_exception[ex_type]

                    if isinstance(replacement, type):
                        raise replacement() from None
                    else:
                        raise replacement from None
                else:
                    raise

        return wrapper

    return decorator
