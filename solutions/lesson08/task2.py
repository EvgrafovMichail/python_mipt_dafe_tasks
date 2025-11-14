from typing import Callable, TypeVar, Any
import time
from functools import wraps
# в комментариях буду указывать на каких стр в презентации что-то схожее
# прост я сам до этого не додумался бы, а так легче аналогично делать
T = TypeVar("T")


def collect_statistic(
    statistics: dict[str, list[float | int]],
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        func_name = func.__name__  # 25-26

        @wraps(func)  # 21
        def wrapper(*args: Any, **kwargs: Any) -> T:
            time_start = time.time()  # 18-19
            result = func(*args, **kwargs)  # 18-19
            execution_time = time.time() - time_start  # 18-19

            if func_name not in statistics:  # 13-14
                statistics[func_name] = [execution_time, 1]
            else:
                avg_time, call_count = statistics[func_name]  # 13-14
                new_call_count = call_count + 1
                new_avg_time = (avg_time * call_count + execution_time) / new_call_count
                statistics[func_name] = [new_avg_time, new_call_count]  # 13-14

            return result  # 18-19

        return wrapper  # 18-19

    return decorator  # 25-26