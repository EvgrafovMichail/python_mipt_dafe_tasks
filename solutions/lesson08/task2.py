import functools
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            spend_time = end_time - start_time

            func_name = func.__name__

            if func_name not in statistics:
                statistics[func_name] = [spend_time, 1]
            else:
                last_avg = statistics[func_name][0]
                last_count = statistics[func_name][1]
                new_count = last_count + 1
                new_avg = (last_avg * last_count + spend_time) / new_count
                statistics[func_name] = [new_avg, new_count]

            return res

        return wrapper

    return decorator
