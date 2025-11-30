from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if retry_amount <= 0:
        raise ValueError
    if timeout_start <= 0:
        raise ValueError
    if timeout_max <= 0:
        raise ValueError
    if backoff_scale <= 0:
        raise ValueError
    if timeout_start > timeout_max:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            timeout = timeout_start

            for num_try in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if not isinstance(exc, backoff_triggers):
                        raise exc from None
                    if num_try == retry_amount - 1:
                        raise exc from None

                jitter_time = uniform(0, 0.5)
                sleep_time = min(timeout + jitter_time, timeout_max)
                sleep(sleep_time)
                timeout = min(timeout_max, timeout * backoff_scale)

        return wrapper

    return decorator
