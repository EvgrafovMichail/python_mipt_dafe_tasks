from typing import Callable
import time
from functools import wraps

def collect_statistic(statistics: dict[str, list[float]]) -> Callable[[Callable], Callable]:
    # ваш код
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            
            timer  = end - start
            name = func.__name__ 
            
            if name in statistics:
                old_timer, count = statistics[name]
                new_count = count + 1
                new_timer = float((old_timer * count + timer ) / new_count)
                statistics[name] = [new_timer, new_count]
            else:
                statistics[name] = [timer , 1]
            
            return result
        
        return wrapper
    
    return decorator