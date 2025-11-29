from functools import wraps
from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def _checks_for_valid(
    retry_amount: int, timeout_start: float, timeout_max: float, backoff_scale: float
) -> None:
    """Функция для проверки валидации входных данных"""

    if not (1 <= retry_amount <= 100):
        raise ValueError

    if not (0 < timeout_start <= 10.0):
        raise ValueError

    if not (0 < timeout_max <= 10.0):
        raise ValueError

    if timeout_start > timeout_max:
        raise ValueError

    if not (0 < backoff_scale <= 10.0):
        raise ValueError


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для повторных запусков функций.

    Args:
        retry_amount: максимальное количество попыток выполнения функции;
        timeout_start: начальное время ожидания перед первой повторной попыткой (в секундах);
        timeout_max: максимальное время ожидания между попытками (в секундах);
        backoff_scale: множитель, на который увеличивается задержка после каждой неудачной попытки;
        backoff_triggers: кортеж типов исключений, при которых нужно выполнить повторный вызов.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        ValueError, если были переданы невозможные аргументы.
    """

    _checks_for_valid(retry_amount, timeout_start, timeout_max, backoff_scale)

    def decor(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep_time = timeout_start

            for now_retry_attemp in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    if now_retry_attemp == retry_amount - 1:
                        raise

                    sleep(sleep_time + uniform(0, 0.5))
                    sleep_time = min(timeout_max, sleep_time * backoff_scale)

                except Exception:
                    raise

        return wrapper

    return decor
