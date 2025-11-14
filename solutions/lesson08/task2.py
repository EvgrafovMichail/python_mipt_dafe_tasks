from typing import Callable, TypeVar, ParamSpec
from functools import wraps
import time

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def get_function(function_: Callable[P, R]) -> Callable[[T], T]:
        @wraps(function_)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_time = time.time()
            val = function_(*args, **kwargs)
            period = time.time() - last_time

            if not function_.__name__ in statistics:
                statistics[function_.__name__] = [0, 0]

            pair = statistics[function_.__name__]
            statistics[function_.__name__][0] = (pair[0] * pair[1] + period) / (pair[1] + 1)
            statistics[function_.__name__][1] = pair[1] + 1

            return val

        return wrapper

    return get_function
