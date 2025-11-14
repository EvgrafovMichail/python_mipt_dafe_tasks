import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def timeit(func):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = func.__name__
            timestart = time.time()
            res = func(*args, **kwargs)
            duration = time.time() - timestart

            if func.__name__ not in statistics:
                statistics[func.__name__] = [duration, 1]

            else:
                aver, times = statistics[func.__name__]
                statistics[func.__name__][1] += 1
                statistics[func.__name__][0] = aver + (duration - aver) / (times + 1)

            return res

        return wrapper

    return timeit
