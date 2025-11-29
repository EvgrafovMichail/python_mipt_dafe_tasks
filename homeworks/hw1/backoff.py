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

    if retry_amount < 1:
        raise ValueError("число попыток должно быть больше нуля")
    if timeout_start <= 0 or timeout_max <= 0 or backoff_scale <= 0:
        raise ValueError("времена ожидания и множитель должны быть больше нуля")
    if timeout_start > timeout_max:
        raise ValueError("начальное время ожидания не может превышать максимальное")

    def decorator(func):
        def wrapper(*args, **kwargs):
            delay = timeout_start
            last_ex = None
            for attempt in range(retry_amount):
                try:
                    res = func(*args, **kwargs)
                    return res
                
                except backoff_triggers as exc:
                    last_ex = exc

                    if attempt == retry_amount - 1:
                        break

                    jitter_time = uniform(0, 0.5)
                    sleep(delay + jitter_time)
                    new_delay = delay * backoff_scale
                    delay = new_delay if new_delay < timeout_max else timeout_max

            raise last_ex

        return wrapper
    
    return decorator
