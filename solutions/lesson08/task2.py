from typing import Callable, TypeVar
import time
from functools import wraps

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    i = 0
    total_time = 0

    def wrapper(func: Callable):
        @wraps(func)
        def timer(*args, **kwargs):
            nonlocal i, total_time
            name = func.__name__
            start = time.time()
            i += 1
            res = func(*args, **kwargs)
            total_time += time.time() - start
            statistics[name] = [total_time / i, i]
            return res

        return timer

    return wrapper
