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
    if any(
        (
            not (1 <= retry_amount <= 100),
            not (0 < timeout_start < 10),
            not (0 < timeout_max < 10),
            not (0 < backoff_scale < 10),
            not all(isinstance(exp, type) for exp in backoff_triggers),
        )
    ):
        raise ValueError

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal timeout_start
            for i in range(retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    sleep(min(timeout_max, timeout_start) + uniform(0, 0.5))
                    timeout_start *= backoff_scale
            raise

        return wrapper

    return decorator
