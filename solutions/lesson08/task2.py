import time
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            duration = end_time - start_time
            func_name = func.__name__

            if func_name in statistics:
                current_avg, current_count = statistics[func_name]
                new_count = current_count + 1
                new_avg = (current_avg * current_count + duration) / new_count
                statistics[func_name] = [new_avg, new_count]
            else:
                statistics[func_name] = [duration, 1]

            return result

        return wrapper

    return decorator
