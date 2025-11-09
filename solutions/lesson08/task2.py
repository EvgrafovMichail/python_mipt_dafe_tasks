from typing import Callable, TypeVar, ParamSpec
import time
from functools import wraps

T = TypeVar("T")

P = ParamSpec("P")
R = TypeVar("R")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def collect_function(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start

            avg, count = statistics.get(func.__name__, [0.0, 0])

            count += 1
            avg = avg + (duration - avg) / count

            statistics[func.__name__] = [avg, count]
            return result

        return wrapper

    return collect_function
