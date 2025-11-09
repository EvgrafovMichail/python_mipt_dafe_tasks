from typing import Callable, TypeVar
from functools import wraps
import time
import math

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float | int]]) -> Callable[[T], T]:
    def decorator(func: Callable[[T], T]) -> Callable[[T], T]:
        func_name = func.__name__
        summa = 0
        counter = 0

        @wraps(func)
        def wrapper(*args: T, **kwargs: T) -> T:
            nonlocal summa, counter
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            working_time = end - start
            summa += working_time
            counter += 1

            if func_name not in statistics:
                statistics[func_name] = [working_time, counter]
            else:
                statistics[func_name] = [summa / counter, counter]
            return result

        return wrapper

    return decorator
