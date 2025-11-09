from typing import Callable, TypeVar
import time, functools

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def collecting(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func.__name__ not in statistics:
                statistics[func.__name__] = [0.0, 0]
            statistics[func.__name__][1] += 1
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            cnt = statistics[func.__name__][1] - 1
            statistics[func.__name__][0] = ((end - start) + statistics[func.__name__][0] * cnt) / (
                cnt + 1
            )
            return result

        return wrapper

    return collecting
