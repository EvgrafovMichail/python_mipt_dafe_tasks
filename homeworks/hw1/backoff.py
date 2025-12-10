from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar
)

P = ParamSpec("P")
R = TypeVar("R")

def _validate_backoff_parameters(
    retry_amount: int,
    timeout_start: float,
    timeout_max: float, 
    backoff_scale: float,
    backoff_triggers: tuple[type[Exception], ...],
) -> None:
    
    if retry_amount < 1 or retry_amount > 100:
        raise ValueError(f"retry_amount should be 1-100, yours{retry_amount}")
    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError(f"timeout_start should be 1-10, yours{timeout_start}")
    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError(f"timeout_max should be 1-10, yours{timeout_max}")
    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError(f"backoff_scale should be 1-10, yours{backoff_scale}")
    if not backoff_triggers:
        raise ValueError("backoff_triggers is empty!")
    for trigger in backoff_triggers:
        if not issubclass(trigger, Exception):
            raise ValueError("All elements backoff_triggers should be Exception")

def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    
    _validate_backoff_parameters(
        retry_amount, timeout_start, timeout_max, backoff_scale, backoff_triggers
    )
       
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: R.kwargs) -> R:
            #начинаем с паузы 
            timeout = timeout_start
            for i in range(retry_amount): #пытаемся несколько раз
                try:                 
                    return func(*args,**kwargs )
                except Exception as error:
                    should_retry = any(isinstance(error, trigger) for trigger in backoff_triggers)
                    if not should_retry or i == retry_amount -1:
                        raise error
                    base_timeout = timeout
                    next_timeout = min(backoff_scale * timeout, timeout_max)
                    sleep_time = base_timeout + uniform(0, 0.5)
                    sleep(sleep_time)
                    timeout = next_timeout
        return wrapper
    return decorator