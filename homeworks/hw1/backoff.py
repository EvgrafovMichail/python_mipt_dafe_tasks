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
    if retry_amount <= 0:
        raise ValueError("retry_amoutn is positive")
    if timeout_start <= 0:
        raise ValueError("timeout_start is positive")
    if timeout_max <= 0:
        raise ValueError("timeout_max is positive")
    if backoff_scale <= 0:
        raise ValueError("backoff_scale is positive")

    def create_backoff(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            current_timeout = timeout_start

            for attempt in range(1, retry_amount + 2):
                try:
                    return func(*args, **kwargs)

                except backoff_triggers as e:
                    if attempt == retry_amount:
                        raise type(e)()

                    sleep(current_timeout + uniform(0, 0.5))

                    current_timeout = min(current_timeout * backoff_scale, timeout_max)

        return wrapper

    return create_backoff
