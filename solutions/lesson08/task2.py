from time import time
from typing import Callable, TypeVar
from functools import wraps

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func):
        name = func.__name__

        if name not in statistics:
            statistics[name] = [0.0, 0]

        @wraps(func)
        def wrapper_functions(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            end = time()

            duration = end - start
            average_time, number_of_calls = statistics[name]
            number_of_calls += 1
            new_average_time = average_time + (duration - average_time) / number_of_calls

            statistics[name] = [new_average_time, number_of_calls]

            return result

        return wrapper_functions

    return decorator
    pass
