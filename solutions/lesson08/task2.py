import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func):
        counter = 0
        dt = 0

        def wrapper(*args, **kwargs):
            nonlocal counter
            nonlocal dt
            t1 = time.time()
            a = func(*args, **kwargs)
            t2 = time.time()
            counter += 1
            dt += t2 - t1
            statistics[func.__name__] = [dt / counter, counter]
            return a

        wrapper.__name__ = func.__name__
        return wrapper

    return decorator
