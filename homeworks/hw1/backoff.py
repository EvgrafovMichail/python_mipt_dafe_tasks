from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


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

    if not isinstance(retry_amount, int) or retry_amount <= 0:
        raise ValueError()
    if not isinstance(timeout_start, (int, float)) or timeout_start <= 0:
        raise ValueError()
    if not isinstance(timeout_max, (int, float)) or timeout_max <= 0:
        raise ValueError()
    if not isinstance(backoff_scale, (int, float)) or backoff_scale <= 0:
        raise ValueError()
    if not isinstance(backoff_triggers, tuple):
        raise ValueError()

    def decorator(func):
        def wrapper(*args, **kwargs):
            wait = timeout_start
            for attempt in range(1, retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    if attempt == retry_amount:
                        return None
                    zadergka = min(wait, timeout_max) + uniform(0, 0.5)
                    sleep(zadergka)
                    wait *= backoff_scale

        return wrapper

    return decorator
