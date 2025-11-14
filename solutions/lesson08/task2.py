import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def checker(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            time_length = end - start
            if func.__name__ not in statistics:
                statistics[func.__name__] = [0.0, 0]
            old_avg, old_count = statistics[func.__name__]
            new_avg = (old_avg * old_count + time_length) / (old_count + 1)
            statistics[func.__name__] = [new_avg, old_count + 1]
            return result

        return wrapper

    return checker
