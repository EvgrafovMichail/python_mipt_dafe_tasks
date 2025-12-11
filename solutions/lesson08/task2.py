from functools import wraps
from time import time
from typing import Callable, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


def collect_statistic(statistics: dict[str, list[float | int]]) -> Callable[P, R]:
    summa = count = 0

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            nonlocal summa, count
            start = time()
            result = func(*args, **kwargs)
            summa += time() - start
            count += 1
            statistics[func.__name__] = [summa / count, count]
            return result

        return inner

    return wrapper
