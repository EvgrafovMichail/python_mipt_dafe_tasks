from functools import wraps
from time import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    # ваш код
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = time() - start
                name = func.__name__
                if name not in statistics:
                    statistics[name] = [0.0, 0]
                old_avg, old_cnt = statistics[name]
                new_cnt = old_cnt + 1
                new_avg = old_avg + (elapsed - old_avg) / new_cnt
                statistics[name][0] = new_avg
                statistics[name][1] = new_cnt

        return wrapper

    return decorator
    pass
