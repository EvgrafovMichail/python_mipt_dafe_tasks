import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def dec(func: T) -> T:
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            t = end - start
            if func.__name__ in statistics:
                avg_time, call_count = statistics[func.__name__]
                avg_time = (avg_time * call_count + t) / (call_count + 1)
                call_count += 1
                statistics[func.__name__] = [avg_time, call_count]
            else:
                call_count = 1
                avg_time = t
                statistics[func.__name__] = [avg_time, call_count]
            return result

        wrapper.__name__ = func.__name__
        return wrapper

    return dec
