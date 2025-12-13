import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(fn):
        def inner(*params, **options):
            inner.__name__ = fn.__name__
            t0 = time.time()
            result = fn(*params, **options)
            delta = time.time() - t0

            if fn.__name__ not in statistics:
                statistics[fn.__name__] = [delta, 1]
            else:
                mean, calls = statistics[fn.__name__]
                statistics[fn.__name__][1] = calls + 1
                statistics[fn.__name__][0] = mean + (delta - mean) / (calls + 1)

            return result

        return inner

    return decorator
