from random import uniform
from time import sleep
from typing import Callable, ParamSpec, TypeVar
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для повторных запусков функций.
    """

    if retry_amount < 1 or retry_amount > 100:
        raise ValueError()
    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError()
    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError()
    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError()

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            current_timeout = timeout_start

            for i in range(retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as e:
                    if i == retry_amount:
                        raise e

                    sleep_time = min(current_timeout, timeout_max) + uniform(0, 0.5)
                    sleep(sleep_time)
                    current_timeout *= backoff_scale

        return wrapper

    return decorator
