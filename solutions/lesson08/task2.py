import time
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")


def collect_statistic(
    statistics: dict[str, list[float, int]],
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_time = time.time()
            val = func(*args, **kwargs)
            period = time.time() - last_time

            if func.__name__ not in statistics:
                statistics[func.__name__] = [0, 0]

            pair = statistics[func.__name__]
            pair[0] = (pair[0] * pair[1] + period) / (pair[1] + 1)
            pair[1] += 1

            return val

        return wrapper

    return decorator
