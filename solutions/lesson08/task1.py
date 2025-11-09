from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    total_income = []

    def get_avg(curr_income: float) -> float:
        nonlocal total_income
        total_income.append(curr_income)
        if len(total_income) > accumulation_period:
            total_income.pop(0)
        return sum(total_income) / len(total_income)

    return get_avg
