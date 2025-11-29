from functools import wraps
from random import uniform
from time import sleep
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if retry_amount < 1 or retry_amount > 100:
        raise ValueError("retry_amount must be between 1 and 100")
    if timeout_start <= 0 or timeout_start > 10:
        raise ValueError("timeout_start must be in (0, 10]")
    if timeout_max <= 0 or timeout_max > 10:
        raise ValueError("timeout_max must be in (0, 10]")
    if backoff_scale <= 0 or backoff_scale > 10:
        raise ValueError("backoff_scale must be in (0, 10]")

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            current_delay = timeout_start
            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as e:
                    if attempt == retry_amount - 1:
                        raise e
                    sleep_time = min(current_delay + uniform(0, 0.5), timeout_max)
                    sleep(sleep_time)
                    current_delay = min(current_delay * backoff_scale, timeout_max)

        return inner

    return wrapper
