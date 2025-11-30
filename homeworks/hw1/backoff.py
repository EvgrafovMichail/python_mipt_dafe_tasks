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
        raise ValueError()
    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError()
    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError()
    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError()

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            time_delay = timeout_start

            for try_num in range(retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as exp:
                    if try_num == retry_amount:
                        raise exp from None

                    if time_delay < timeout_max:
                        delay = time_delay + uniform(0, 0.5)
                    else:
                        delay = timeout_max
                    if delay >= timeout_max:
                        delay = timeout_max

                    sleep(delay)
                    time_delay *= backoff_scale

        return wrapper

    return decorator
