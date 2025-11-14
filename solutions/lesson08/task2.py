import time
from functools import wraps
from typing import Any, Callable, TypeVar


T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    coef = 0.003  # доп. коэффициент для компенсации погрешности

    def decor(func: T) -> T:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            start_time = time.time()
            result = func(*args, **kwargs)
            differ_time = time.time() - start_time - coef

            func_name = func.__name__
            if func_name in statistics:
                time_avg, call_count = statistics[func_name]

                call_count += 1
                pre_sum_time = time_avg * (call_count - 1)
                time_avg = (pre_sum_time + differ_time) / call_count

                statistics[func_name] = [round(time_avg, 2), call_count]
            else:
                statistics[func_name] = [round(differ_time, 2), 1]
            return result

        return wrapper

    return decor
