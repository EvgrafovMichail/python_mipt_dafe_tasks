import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def func_dec(func):
        f_name = func.__name__

        if f_name not in statistics:
            statistics[func.__name__] = [0.0, 0]

        @wraps(func)
        def func_inf(*args, **kwargs):
            time_start = time.time()
            res = func(*args, **kwargs)
            delta = time_start - time.time()

            time_avg = statistics[f_name][0]
            call_counter = statistics[f_name][1]

            call_counter += 1
            time_avg = (time_avg * (call_counter - 1) + delta) / call_counter
            statistics[f_name] = [time_avg, call_counter]
            return res

        return func_inf

    return func_dec
