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
    if not (1 <= retry_amount <= 100 and 0 < timeout_start <= 10 and 0 < timeout_max <= 10 and 0 < backoff_scale <= 10 and timeout_start <= timeout_max):
        raise ValueError("Invalid arguments")
    
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception = None
            current_delay = timeout_start
            for attempt in range(retry_amount):
                try:
                    result_value = func(*args, **kwargs)
                    return result_value
                except backoff_triggers as exc:
                    last_exception = exc
                    if attempt == retry_amount - 1:
                        break
                    jitter = uniform(0, 0.5)
                    wait_time = min(current_delay + jitter, timeout_max)
                    sleep(wait_time)
                    current_delay = min(current_delay * backoff_scale, timeout_max)
            if last_exception is not None:
                raise last_exception
        return wrapper
    return decorator