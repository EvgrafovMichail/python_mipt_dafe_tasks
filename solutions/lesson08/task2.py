import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            full_time = end_time - start_time
            function_name = func.__name__
            if function_name not in statistics:
                statistics[function_name] = [full_time, 1]
            else:
                old_mean_arithmetic, count = statistics[function_name]
                new_mean_arithmetic = (old_mean_arithmetic * count + full_time) / (count + 1)
                statistics[function_name] = [new_mean_arithmetic, count + 1]
            return result

        return wrapper

    return decorator
