import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def wrapper(func):
        @wraps(func)
        def clock(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start

            if func.__name__ in statistics:
                statistics[func.__name__][0] = (
                    statistics[func.__name__][0] * statistics[func.__name__][1] + duration
                ) / (statistics[func.__name__][1] + 1)
                statistics[func.__name__][1] += 1
            else:
                statistics[func.__name__] = [duration, 1]
            return result

        return clock

    return wrapper
