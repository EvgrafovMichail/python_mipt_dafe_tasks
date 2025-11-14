from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    values = []
    current_index = 0
    count = 0
    
    def get_avg(x: float) -> float:
        nonlocal current_index, count
        
        if count < accumulation_period:
            values.append(x)
            count += 1
        else:
            values[current_index] = x
            current_index = (current_index + 1) % accumulation_period
        
        return sum(values) / count
    
    return get_avg