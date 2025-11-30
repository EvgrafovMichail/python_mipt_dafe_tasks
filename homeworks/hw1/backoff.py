import functools
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

    if retry_amount <= 0 or timeout_start <= 0 or timeout_max <= 0 or backoff_scale <= 0:
        raise ValueError

    if not isinstance(backoff_triggers, tuple) or not all(
        issubclass(exc, Exception) for exc in backoff_triggers
    ):
        raise ValueError

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = timeout_start

            for attemp in range(1, retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    if attemp == retry_amount:
                        raise

                    jitter = uniform(0, 0.5)
                    sleep_time = min(delay, timeout_max) + jitter
                    sleep(sleep_time)

                    delay = min(delay * backoff_scale, timeout_max)

        return wrapper

    return decorator
