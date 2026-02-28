import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def _collect_statistic(func) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            start_time = time.time()
            res = func(*args, **kwargs)
            delta_time = time.time() - start_time
            if func_name not in statistics:
                statistics[func_name] = [delta_time, 1]
            else:
                time_avg, counter = statistics[func_name]
                statistics[func_name] = [
                    (time_avg * counter + delta_time) / (counter + 1),
                    counter + 1,
                ]
            return res

        return wrapper

    return _collect_statistic
