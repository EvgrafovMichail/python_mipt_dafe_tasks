import functools
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
    if not 0 < retry_amount <= 100 or not isinstance(retry_amount, int):
        raise ValueError
    elif not isinstance(timeout_start, (int, float)) or not 0 < timeout_start < 10:
        raise ValueError
    elif not isinstance(timeout_max, (int, float)) or not 0 < timeout_max <= 10:
        raise ValueError
    elif not isinstance(backoff_scale, (int, float)) or not 0 < backoff_scale < 10:
        raise ValueError

    def decorator(func):
        @functools.wraps(func)
        def wraps(*args, **kwargs):
            current_timeout = timeout_start
            attempts_remaining = retry_amount
            while attempts_remaining > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts_remaining -= 1
                    if not isinstance(e, backoff_triggers):
                        raise e from None
                    if attempts_remaining == 0:
                        raise e from None
                    jitter = uniform(0, 0.5)
                    total_sleep_time = min(current_timeout + jitter, timeout_max)
                    sleep(total_sleep_time)
                    current_timeout = min(current_timeout * backoff_scale, timeout_max)

        return wraps

    return decorator
