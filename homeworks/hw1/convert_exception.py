from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P") # Эти записи - гарантия того, что входные и выходные параметры декоратора будут такими же, как и у самой функции
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

    def decorator_replacement_exclusive(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Получаем тип пойманного исключения
                caught_exception_type = type(e)

                for exception_pair in exception_to_api_exception.items():
                    internal_exc_type = exception_pair[0]  # Тип внутреннего исключения
                    api_exc = exception_pair[1]  # API-исключение

                    # Простая проверка: точное совпадение типов
                    if caught_exception_type == internal_exc_type:
                        # Явная проверка типа
                        if type(api_exc) is type:
                            raise api_exc() from None # True, потому что ApiValueError - это класс
                        else:
                            raise api_exc from None   # False, потому что экземпляр - это объект ApiValueError

                raise

        return wrapper

    return decorator_replacement_exclusive