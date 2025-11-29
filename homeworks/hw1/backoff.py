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
        raise ValueError()

    def decorator(func):
        def wrapper(*args, **kwargs):
            zader = timeout_start

            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    if attempt == retry_amount - 1:
                        raise Exception

                    jitter_time = uniform(0, 0.5)
                    sleep(zader + jitter_time)
                    if zader * backoff_scale > timeout_max:
                        zader = timeout_max
                    else:
                        zader *= backoff_scale

        return wrapper

    return decorator
