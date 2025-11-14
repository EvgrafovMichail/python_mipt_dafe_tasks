import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    calls = 0

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            calls += 1
            start_time = time.time()
            res = func(*args, **kwargs)
            statistics[func.__name__] = [time.time() - start_time, calls]
            return res

        return wrapper

    return decorator
