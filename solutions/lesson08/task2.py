from functools import wraps
from time import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            res = func(*args, **kwargs)
            end_time = time() - start_time

            func_name = func.__name__

            if func_name in statistics:
                old_average, count = statistics[func_name]
                statistics[func_name] = [(old_average * count + end_time) / (count + 1), count + 1]
            else:
                statistics[func_name] = [end_time, 1]

            return res

        return wrapper

    return decorator
