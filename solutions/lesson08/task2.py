from typing import Callable, TypeVar
import time
from functools import wraps

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    # ваш код

    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time - start_time
            func_name = func.__name__

            if func_name in statistics:
                current_data = statistics[func_name]
                current_avg = current_data[0]
                current_count = current_data[1]

                new_count = current_count + 1
                new_avg = (current_avg * current_count + exec_time) / new_count

                statistics[func_name] = [new_avg, new_count]

            else:
                statistics[func_name] = [exec_time, 1]

            return result

        return wrapper

    return decorator
