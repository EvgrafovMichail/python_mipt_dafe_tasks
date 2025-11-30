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

    if (
        (retry_amount <= 0 or retry_amount > 100)
        or (timeout_start <= 0 or timeout_start > 10)
        or (timeout_max <= 0 or timeout_max > 10)
        or (backoff_scale <= 0 or backoff_scale > 10)
    ):
        raise ValueError("Invalid value")

    def decorator(func: Callable[P, R]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal backoff_triggers
            timeout = timeout_start

            for retry in range(retry_amount + 1):
                try:
                    return func(*args, **kwargs)

                except backoff_triggers as exc:
                    if retry == retry_amount:
                        raise exc

                    timeout = min(timeout, timeout_max)
                    sleep_timeout = timeout + uniform(0, 0.5)
                    sleep(sleep_timeout)

                    timeout *= backoff_scale

                except Exception:
                    raise

        return wrapper

    return decorator
