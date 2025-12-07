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
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                mapped = None
                types = []
                for exc_key in exception_to_api_exception:
                    if issubclass(type(exc), exc_key):
                        types.append(exc_key)

                Type = None

                for cl in types:
                    if all(issubclass(cl, other) for other in types if other is not cl):
                        Type = cl

                if Type is None:
                    raise

                mapped = exception_to_api_exception[Type]

                if mapped is None:
                    raise

                if isinstance(mapped, type) and issubclass(mapped, Exception):
                    raise mapped() from None
                else:
                    raise mapped from None

        return wrapper

    return decorator
