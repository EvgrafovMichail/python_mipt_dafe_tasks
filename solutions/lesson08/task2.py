import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    
    def decorator(func: T) -> T:
        metrics = [0, 0.0] 
        
        def wrapper(*args, **kwargs):
            time.sleep(0.001) #Для точности времени, пусть чуть стабилизируется 

            start_time = time.time()
            func_res = func(*args, **kwargs)
            end_time = time.time()
            
            spend_time = end_time - start_time
            metrics[0] += 1        
            metrics[1] += spend_time  

            average_time = metrics[1] / metrics[0]
            statistics[func.__name__] = [average_time, metrics[0]]
            
            return func_res

        wrapper.__name__ = func.__name__
        return wrapper  
    
    return decorator