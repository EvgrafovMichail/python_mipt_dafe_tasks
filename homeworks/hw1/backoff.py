from time import sleep
from random import uniform
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

    if retry_amount < 1 or timeout_start <= 0 or timeout_max <= 0 or backoff_scale <= 0:
        raise ValueError("Parameters must be positive")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            
            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                
                except backoff_triggers as e:
                    
                    if attempt == retry_amount - 1:
                        raise e
                    
                    delay = timeout_start * (backoff_scale ** attempt)
                    
                    if delay > timeout_max:
                        delay = timeout_max
                    jitter = uniform(0, 0.5)
                    total_delay = delay + jitter
                    
                    sleep(total_delay)
            
            return func(*args, **kwargs)

        return wrapper
    return decorator