import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def deccorator(function: Callable):
        accumulator, counter = 0, 0

        @wraps(function)
        def wrapper(*args: ..., **kwargs: ...) -> T:
            nonlocal statistics
            nonlocal accumulator, counter

            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()

            counter += 1

            accumulator += end - start

            statistics[function.__name__] = [accumulator / counter, counter]

            return result

        return wrapper

    return deccorator
