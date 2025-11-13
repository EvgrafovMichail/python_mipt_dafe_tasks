import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: Callable[[T], T]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()

            if func.__name__ in statistics:
                statistics[func.__name__][1] += 1
                statistics[func.__name__][0] = (
                    statistics[func.__name__][0] * (statistics[func.__name__][1] - 1)
                    + time_end
                    - time_start
                ) / statistics[func.__name__][1]
            else:
                statistics[func.__name__] = [time_end - time_start, 1]

            return result

        return wrapper

    return decorator
