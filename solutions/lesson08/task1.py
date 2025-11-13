from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    income = []
    def get_avg(x: float) -> float:
        income.append(x)
        if len(income) <= accumulation_period:
            return sum(income) / len(income)
        else:
            income.pop(0)
            return sum(income) / len(income)
    return get_avg