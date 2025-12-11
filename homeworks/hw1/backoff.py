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
    my_args = (retry_amount, timeout_start, timeout_max, backoff_scale)
    for current in my_args:
        if current <= 0:
            raise ValueError

    def decor(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = timeout_start
            for i in range(0, retry_amount):
                try:
                    result = func(*args, **kwargs)
                except backoff_triggers as exc:
                    if not isinstance(exc, backoff_triggers):
                        raise
                    if i < retry_amount - 1:
                        jitter_time = uniform(0, 0.5)
                        sleep_time = min(current_time, timeout_max)
                        sleep(sleep_time + jitter_time)
                        current_time = backoff_scale * current_time
                    else:
                        raise
                else:
                    return result

        return wrapper

    return decor
