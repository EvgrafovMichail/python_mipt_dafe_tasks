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
    timeout_max: float = 9.99,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if (
        (not (1 <= retry_amount <= 100))
        or (not (0 < timeout_start < 10))
        or (not (0 < timeout_max < 10))
        or (not (0 < backoff_scale < 10))
    ):
        raise ValueError("Input_Error")

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> None:
            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as e:
                    if attempt == retry_amount - 1:
                        raise e
                    time = uniform(0, 0.5) + timeout_start * backoff_scale**attempt
                    if time <= timeout_max:
                        sleep(time)
                    else:
                        sleep(timeout_max)
                    continue

        return inner

    return wrapper
