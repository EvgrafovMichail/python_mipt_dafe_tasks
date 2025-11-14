import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def fabric(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if func_name not in statistics:
                statistics[func_name] = [0.0, 0]
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            statistics[func_name][0] = (
                statistics[func_name][0] * statistics[func_name][1] + total_time
            ) / (statistics[func_name][1] + 1)
            statistics[func_name][1] += 1
            return result

        return wrapper

    return fabric
