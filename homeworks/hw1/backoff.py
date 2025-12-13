import time
from functools import wraps
from random import uniform
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

    if (
        retry_amount < 1
        or retry_amount > 100
        or timeout_start <= 0
        or timeout_start > 10
        or timeout_max <= 0
        or timeout_max > 10
        or backoff_scale <= 0
        or backoff_scale > 10
    ):
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            current_timeout = timeout_start
            retries = 0

            while True:
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    retries += 1

                    if any(isinstance(e, i) for i in backoff_triggers):
                        if retries > retry_amount:
                            raise e

                        sleep_time = current_timeout + uniform(0, 0.5)
                        sleep_time = min(sleep_time, timeout_max)
                        time.sleep(sleep_time)

                        current_timeout = min(backoff_scale * current_timeout, timeout_max)

                    else:
                        raise e

        return wrapper

    return decorator
