import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(f):
        def wrap(*p, **q):
            wrap.__name__ = f.__name__
            s = time.time()
            r = f(*p, **q)
            t = time.time() - s

            if f.__name__ not in statistics:
                statistics[f.__name__] = [t, 1]
            else:
                m, c = statistics[f.__name__]
                statistics[f.__name__][1] = c + 1
                statistics[f.__name__][0] = m + (t - m) / (c + 1)

            return r

        return wrap

    return decorator
