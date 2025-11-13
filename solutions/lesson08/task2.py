from typing import Callable, TypeVar
import time
from functools import wraps
T = TypeVar("T")

def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            run = func(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            func_name = func.__name__
            if func_name in statistics:
                statistics[func_name][1] += 1
                statistics[func_name][0] = (statistics[func_name][0] * (statistics[func_name][1] - 1) + total_time) / statistics[func_name][1]
            else:
                statistics[func_name] = [total_time, 1]
            return run
        return wrapped
    return decorator
    