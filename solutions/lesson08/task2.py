import functools
import time
from typing import Any, Callable, Dict, List, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: Dict[str, List[Any]]) -> Callable[[T], T]:
    def decorator(func: T) -> T:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.time()
                duration = end - start
                name = func.__name__

                if name not in statistics:
                    statistics[name] = [0.0, 0]

                avg_time, calls = statistics[name]
                calls += 1
                avg_time = (avg_time * (calls - 1) + duration) / calls
                statistics[name] = [avg_time, calls]

        return wrapper

    return decorator
