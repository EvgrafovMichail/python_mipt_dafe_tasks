from typing import Callable, TypeVar
import time

T = TypeVar("T")

def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    def decorator(func):
        def wrapped(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            name = func.__name__
            
            if name not in statistics:
                statistics[name] = [duration, 1]
            else:
                old_avg, count = statistics[name]
                total = old_avg * count + duration
                count += 1
                new_avg = total / count
                statistics[name] = [new_avg, count]
            
            return result
        
        wrapped.__name__ = func.__name__
        return wrapped
    return decorator