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

    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            try:
                res =  func(*args, **kwargs)
                return res
            except Exception as exp:
                exp_type = type(exp)
                if exp_type in exception_to_api_exception:
                    api_exception = exception_to_api_exception[exp_type]
                    raise api_exception from None
                raise exp
        return inner
    return wrapper
                    
#@convert_exceptions_to_api_compitable_ones(
#    exception_to_api_exception={ValueError: ValueError("it is worked"), KeyError: KeyError('Fail')}
#)
#def raise_key_error() -> None:
#    raise KeyError("missed")

#raise_key_error()