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
    if (
        retry_amount < 1
        or retry_amount > 100
        or timeout_start <= 0
        or timeout_start > 10
        or timeout_max <= 0
        or timeout_max > 10
        or backoff_scale <= 0
        or backoff_scale > 10
        or timeout_start > timeout_max
    ):
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            e = None
            for curr_try in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as exception:
                    e = exception
                    if curr_try != retry_amount - 1:
                        curr_pause = min(
                            timeout_start * backoff_scale**curr_try, timeout_max
                        ) + uniform(0, 0.5)
                        sleep(curr_pause)
            raise e

        return wrapper

    return decorator
