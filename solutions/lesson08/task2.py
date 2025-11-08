import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: Callable[[T], T]) -> Callable[[T], T]:
        nonlocal statistics

        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            start_time = time.time()
            result: T = func(*args, **kwargs)
            res_time = time.time() - start_time
            func_name = func.__name__
            if func.__name__ in statistics.keys():
                statistics[func_name][0] = (statistics[func_name][0] + res_time) / 2
                statistics[func_name][1] += 1
            else:
                statistics[func_name] = [res_time, 1]
            return result

        return wrapper

    return decorator
