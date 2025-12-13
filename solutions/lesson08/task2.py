import functools
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(
    statistics: dict[str, list[float, int]],
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def wrapper(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def initer(*args, **kwargs) -> T:
            start = time.time()
            res = func(*args, **kwargs)

            if func.__name__ not in statistics:
                statistics[func.__name__] = [time.time() - start, 1]
            else:
                old_sum_time = statistics[func.__name__][0] * statistics[func.__name__][1]
                statistics[func.__name__][1] += 1
                statistics[func.__name__][0] = (old_sum_time + time.time() - start) / statistics[
                    func.__name__
                ][1]

            return res

        return initer

    return wrapper
