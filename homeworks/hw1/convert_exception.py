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

    def call(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                if type(exc) in exception_to_api_exception:
                    return_exc = exception_to_api_exception[type(exc)]
                    if isinstance(return_exc, type) and issubclass(return_exc, Exception):
                        return_exc = return_exc()
                        raise return_exc
                    else:
                        raise exception_to_api_exception[type(exc)]
                else:
                    raise

        return wrapper

    return call


pass
