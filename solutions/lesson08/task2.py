import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def collect_statistic(
    stats_dict: dict[str, list[float | int]],
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        function_name = func.__name__

        def wrapper(*args: Any, **kwargs: Any) -> T:
            start_time = time.perf_counter()
            try:
                output = func(*args, **kwargs)
                return output
            finally:
                time_taken = time.perf_counter() - start_time

                if function_name in stats_dict:
                    current_avg, current_count = stats_dict[function_name]
                    updated_count = current_count + 1
                    updated_avg = current_avg + (time_taken - current_avg) / updated_count
                    stats_dict[function_name] = [updated_avg, updated_count]
                else:
                    stats_dict[function_name] = [time_taken, 1]

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        wrapper.__qualname__ = func.__qualname__
        wrapper.__annotations__ = func.__annotations__

        return wrapper

    return decorator
