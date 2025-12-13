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

    # ваш код
    if not 0 < retry_amount <= 100 or not isinstance(retry_amount, int):
        raise ValueError
    elif not isinstance(timeout_max, (int, float)) or not 0 < timeout_max <= 10:
        raise ValueError
    elif not isinstance(timeout_start, (int, float)) or not 0 < timeout_start < 10:
        raise ValueError
    elif not isinstance(backoff_scale, (int, float)) or not 0 < backoff_scale < 10:
        raise ValueError

    def decorator(func):
        def wrapper(*args, **kwargs):
            current_timeout = timeout_start
            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if not isinstance(e, backoff_triggers) or attempt == retry_amount - 1:
                        raise
                    time = min(current_timeout, timeout_max)
                    jitter_time = uniform(0, 0.5)
                    sleep(time + jitter_time)
                    current_timeout = min(current_timeout * backoff_scale, timeout_max)

        return wrapper

    return decorator
