import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def func_analis(func: T) -> T:
        @wraps(func)
        def wrapper(*args: ..., **kwargs: ...) -> T:
            time_start = time.time()
            result = func(*args, **kwargs)
            all_time = time.time() - time_start

            if func.__name__ in statistics:
                time_avg = statistics[func.__name__][0]
                call_counter = statistics[func.__name__][1]
                time_avg = (time_avg * call_counter + all_time) / (call_counter + 1)
                call_counter += 1
                statistics[func.__name__] = [time_avg, call_counter]

            else:
                statistics[func.__name__] = [all_time, 1]

            return result

        return wrapper

    return func_analis
