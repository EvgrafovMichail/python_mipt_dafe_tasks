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

    def decorator(func: Callable[[P], R]) -> Callable[[P], R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exc_from_lst = None
                for exc, api_exc in exception_to_api_exception.items():
                    if isinstance(e, exc):
                        exc_from_lst = api_exc
                        break

                if exc_from_lst:
                    raise exc_from_lst from None
                else:
                    raise e

        return wrapper

    return decorator
