from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def is_validate(retry_amount, timeout_start, timeout_max, backoff_scale):
    check_type = (
        isinstance(retry_amount, int)
        and isinstance(timeout_start, (int, float))
        and isinstance(timeout_max, (int, float))
        and isinstance(backoff_scale, (int, float))
    )

    check_value = (
        (1 <= retry_amount <= 100)
        and (0 < timeout_start <= 10)
        and (0 < timeout_max <= 10)
        and (0 < backoff_scale <= 10)
    )

    return check_type and check_value


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

    if not is_validate(retry_amount, timeout_start, timeout_max, backoff_scale):
        raise ValueError

    def decorator(func):
        def wrapper(*args, **kwargs):
            curr_delay = timeout_start
            attempts = 0

            while attempts <= retry_amount:
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if not any(isinstance(exc, trigger) for trigger in backoff_triggers):
                        raise exc from None

                    attempts += 1
                    if attempts > retry_amount:
                        raise exc from None

                    delay = min(curr_delay, timeout_max)
                    jitter_time = uniform(0, 0.5)
                    delay += jitter_time
                    sleep(delay)
                    curr_delay *= backoff_scale

            raise

        return wrapper

    return decorator
