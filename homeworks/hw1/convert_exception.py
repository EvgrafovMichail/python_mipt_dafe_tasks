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

    # ваш код

    def deco_ex_convert(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as exc:
                for exc_key, api_similar in exception_to_api_exception.items():
                    if isinstance(exc, exc_key):
                        if isinstance(api_similar, type): # Проверка на класс!!!
                            raise api_similar() # Создаем экземпляр, если он на самом деле класс
                        raise api_similar
                raise exc
        return wrapper
    return deco_ex_convert 