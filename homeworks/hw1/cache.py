from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    Args:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """

    try:
        int_capacity: int = int(round(capacity))

    except Exception:
        raise TypeError

    else:
        if int_capacity < 1:
            raise ValueError

        def decorator(func: Callable[P, R]) -> Callable[P, R]:
            """Ключ в виде кортежа (args, кортеж kwargs)"""
            """Значение при ключе - это возвращаемое значение"""
            """kwargs преобразуется в кортеж (ключ, значение)"""

            lru_dict: dict[tuple[tuple[object], tuple[object, object]], object] = {}

            """Порядок ключей в словаре является очередью"""
            """Первый ключ - последний в очереди"""
            """Последний ключ - первый в очереди"""

            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                """
                Кортеж (args, кортеж kwargs)
                Асимптотическая сложность линейно зависит
                от количества именованных аргументов
                """
                args_pair = (args, tuple(kwargs.items()))

                """Проверка на наличие набора аргументов в lru_dict"""
                if args_pair not in lru_dict.keys():
                    """Добавляем отсутствующий набор агрументов"""
                    lru_dict[args_pair] = func(*args, **kwargs)

                    """Удаление последнего в очереди """
                    if len(lru_dict) > int_capacity:
                        lru_dict.pop(next(iter(lru_dict)), None)

                else:
                    """Меняем порядок набора аргумента"""
                    lru_dict[args_pair] = lru_dict.pop(args_pair, None)

                return lru_dict[args_pair]

            return wrapper

        return decorator
