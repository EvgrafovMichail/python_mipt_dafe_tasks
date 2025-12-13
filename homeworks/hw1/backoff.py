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

    if not isinstance(retry_amount, int) or retry_amount < 1:
        raise ValueError

    for x in (timeout_start, timeout_max, backoff_scale):
        if not isinstance(x, (int, float)) or x <= 0:
            raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: ..., **kwargs: ...) -> R:
            timeout = timeout_start
            for attempt in range(1, retry_amount + 1):
                try:
                    return func(*args, **kwargs)

                except backoff_triggers as exc:
                    if attempt == retry_amount:
                        raise exc
                    
                    jitter_time = uniform(0, 0.5)
                    sleep(min(timeout + jitter_time, timeout_max))
                    timeout *= backoff_scale
                    timeout = min(timeout, timeout_max)

        return wrapper

    return decorator
