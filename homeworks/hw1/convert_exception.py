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

    def decorator(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(exception_to_api_exception.keys()) as exc:
                raise exception_to_api_exception[type(exc)] from None
            except Exception:
                raise

        return wrapper

    return decorator


"""
@convert_exceptions_to_api_compitable_ones(
exception_to_api_exception={ValueError: ValueError("it is worked")}
)
def raise_key_error() -> None:
    raise KeyError("missed")

raise_key_error()

"""

"""
def decorator(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(exception_to_api_exception.keys()) as exc:
                raise exception_to_api_exception[type(exc)] from None
            except Exception:
                raise
        return wrapper
    return decorator
"""

"""РАБОТАЕТ!!!
except tuple(exception_to_api_exception.keys()) as exc:
            # Находим точный класс из словаря, который соответствует пойманному исключению
            for exc_type, api_exc in exception_to_api_exception.items():
                if isinstance(exc, exc_type):  # Проверяем принадлежность к классу/подклассу
                    if isinstance(api_exc, type):
                        raise api_exc() from None
                    else:
                        raise api_exc from None
            # Если вдруг не нашли (маловероятно), пробрасываем оригинал
            raise
"""
""" 
            except Exception as exc:
                if type(exc) in exception_to_api_exception:
                    raise exception_to_api_exception[type(exc)] from None
                raise
"""
