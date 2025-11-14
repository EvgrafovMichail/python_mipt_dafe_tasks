from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    # ваш код
    income_num = []

    def get_avg(x):
        income_num.append(x)
        if len(income_num) > accumulation_period:
            income_num.pop(0)
        result = sum(income_num) / len(income_num)
        return result
    
    return get_avg