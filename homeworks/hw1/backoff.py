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
    if retry_amount <= 0 or retry_amount > 100:
        raise ValueError("retry_amount должен быть от 1 до 100")

    if timeout_start <= 0 or timeout_start > 10:
        raise ValueError("timeout_start должен быть от 0 до 10")

    if timeout_max <= 0 or timeout_max > 10:
        raise ValueError("timeout_max должен быть от 0 до 10")

    if backoff_scale <= 0 or backoff_scale > 10:
        raise ValueError("backoff_scale должен быть от 0 до 10")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            current_timeout = timeout_start
            attempts_left = retry_amount

            while attempts_left > 0:
                try:
                    return func(*args, **kwargs)

                except backoff_triggers as error:
                    attempts_left -= 1

                    if attempts_left == 0:
                        raise error

                    random_jitter = uniform(0, 0.5)
                    sleep_time = min(current_timeout + random_jitter, timeout_max)

                    sleep(sleep_time)

                    current_timeout = min(current_timeout * backoff_scale, timeout_max)

                except Exception as error:
                    raise error

        return wrapper

    return decorator
