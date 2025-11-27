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
    if retry_amount < 1 or retry_amount > 100:
        raise ValueError

    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError

    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError

    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError

    if timeout_start > timeout_max:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception = None
            current_timeout = timeout_start

            for num_try in range(retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as e:
                    last_exception = e

                    if num_try == retry_amount:
                        raise last_exception

                    jitter = uniform(0, 0.5)
                    total_sleep_time = min(current_timeout + jitter, timeout_max)

                    sleep(total_sleep_time)

                    current_timeout *= backoff_scale
                    if current_timeout > timeout_max:
                        current_timeout = timeout_max

            raise last_exception

        return wrapper

    return decorator
