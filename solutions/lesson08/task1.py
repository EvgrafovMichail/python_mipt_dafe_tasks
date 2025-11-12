from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    period_revenue_value = [] 
    def get_avg(m: int) -> float:
        period_revenue_value.append(m)
        if len(period_revenue_value) > accumulation_period:
            period_revenue_value.pop(0)
        return sum(period_revenue_value) / len(period_revenue_value)
    return get_avg