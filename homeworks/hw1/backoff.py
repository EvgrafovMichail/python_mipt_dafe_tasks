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
    if not is_valid_args(retry_amount, timeout_start, timeout_max, backoff_scale):
        raise ValueError("Args must be positive")

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            nonlocal retry_amount, timeout_start, timeout_max, backoff_scale, backoff_triggers
            last_exc = backoff_triggers[0]
            while retry_amount != 0:
                retry_amount -= 1
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as exc:
                    for cor_exc in backoff_triggers:
                        if isinstance(exc, cor_exc):
                            sleep(timeout_start + uniform(0, 0.5))
                            if timeout_start * backoff_scale <= timeout_max:
                                timeout_start *= backoff_scale
                            last_exc = exc
                            break
            raise last_exc

        return inner

    return wrapper


def is_valid_args(lim: int, start: float, end: float, scale: float) -> bool:
    return (1 < lim < 100) and (0 < start <= 10) and (0 < end <= 10) and (0 < scale <= 10)
