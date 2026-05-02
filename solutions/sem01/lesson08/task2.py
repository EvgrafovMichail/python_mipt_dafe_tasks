import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics) -> Callable[[T], T]:
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            times = time.time() - time_start
            func_name = func.__name__
            if func_name in statistics:
                curr_avg, call_count = statistics[func_name]
                avg_new_time = (curr_avg * call_count + times) / (call_count + 1)
                statistics[func_name] = [avg_new_time, call_count + 1]
            else:
                statistics[func_name] = [times, 1]
            return result

        return wrapper

    return timeit
