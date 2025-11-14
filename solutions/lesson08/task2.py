from functools import wraps
from time import time
from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def collect_function(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time()
            result = func(*args, **kwargs)
            duration = time() - start

            avg, count = statistics.get(func.__name__, [0.0, 0])

            count += 1
            avg = avg + (duration - avg) / count

            statistics[func.__name__] = [avg, count]
            return result

        return wrapper

    return collect_function
