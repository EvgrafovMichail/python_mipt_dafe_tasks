import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()
            process_time = time_end - time_start
            name = func.__name__

            if name not in statistics:
                statistics[name] = [process_time, 1]
            else:
                old_time = statistics[name][0]
                old_cnt = statistics[name][1]
                statistics[name][0] = (old_time * old_cnt + process_time) / (old_cnt + 1)
                statistics[name][1] = old_cnt + 1
            return result

        return wrapper

    return decorator
