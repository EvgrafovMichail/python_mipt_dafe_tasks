import time
from typing import Callable, TypeVar

T = TypeVar("T")

def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    def decor(func: Calable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()

            statistics.setdefault(func.__name__, [0, 0])
            count = statistics[func.__name__][1]
            statistics[func.__name__][0] = count * statistics[func.__name__][0] + end_time - start_time
            statistics[func.__name__][0] /= count + 1
            statistics[func.__name__][1] += 1

            return res

        return wrapper
    return decor
    
    # ваш код
    pass
