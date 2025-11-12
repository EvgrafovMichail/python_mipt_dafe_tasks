import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        # func_time = 0
        count = 0

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # nonlocal func_time
            nonlocal count
            nonlocal statistics
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()
            if func.__name__ in statistics:
                prev_time = statistics[func.__name__][0] * count
            else:
                prev_time = 0
            count += 1
            statistics[func.__name__] = [(prev_time + (time_end - time_start)) / count, count]
            return result

        return wrapper

    return decorator
