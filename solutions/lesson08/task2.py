from time import time
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

R = TypeVar("R")
P = ParamSpec("P")


def collect_statistic(statistics: dict[str, list[float | int]]) -> Callable[P, R]:
    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time()
            result = func(*args, **kwargs)
            during = time() - start
            if func.__name__ in statistics:
                prev_stat = statistics[func.__name__]
                statistics[func.__name__] = [
                    (prev_stat[0] * prev_stat[1] + during) / prev_stat[1] + 1,
                    prev_stat[1] + 1,
                ]
            else:
                statistics[func.__name__] = [during, 1]
            return result

        return inner

    return wrapper
