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
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if not isinstance(retry_amount, int) or not (1 <= retry_amount <= 100):
        raise ValueError
    if not isinstance(timeout_start, (int, float)) or not (0 < timeout_start < 10):
        raise ValueError
    if not isinstance(timeout_max, (int, float)) or not (0 < timeout_max < 10):
        raise ValueError
    if not isinstance(backoff_scale, (int, float)) or not (0 < backoff_scale < 10):
        raise ValueError
    if not isinstance(backoff_triggers, tuple):
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            delay = timeout_start

            attempt = 0
            while attempt <= retry_amount:
                try:
                    return func(*args, **kwargs)

                except backoff_triggers:
                    if attempt == retry_amount:
                        raise

                    sleep(min(delay, timeout_max) + uniform(0, 0.5))
                    delay *= backoff_scale
                    attempt += 1

        return wrapper

    return decorator
