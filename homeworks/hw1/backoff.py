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

    validate_args = {
        (retry_amount, int, lambda x: 1 <= x <= 100, "retry_amount shoud be int from 1 to 100"),
        (
            timeout_max,
            (float, int),
            lambda x: 0 < x <= 10,
            "timeout_max shoud be float in interval (0, 10]",
        ),
        (
            timeout_start,
            (float, int),
            lambda x: 0 < x <= 10,
            "timeout_start shoud be float in interval (0, 10]",
        ),
        (
            backoff_scale,
            (float, int),
            lambda x: 0 < x < 10,
            "backoff_scale shoud be float in interval (0, 10)",
        ),
    }

    for value, vartype, condition, err in validate_args:
        if not isinstance(value, vartype) or not condition(value):
            raise ValueError(err)

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try_count = 1
            timeout = timeout_start

            while True:
                try:
                    return function(*args, **kwargs)
                except backoff_triggers as exc:
                    try_count += 1

                    if try_count > retry_amount:
                        raise exc

                    jitter_time = uniform(0, 0.5)

                    sleep(jitter_time + timeout)

                    timeout = min(timeout * backoff_scale, timeout_max)

        return wrapper

    return decorator
