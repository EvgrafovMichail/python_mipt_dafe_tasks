from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    incomes = []

    def get_avg(d):
        nonlocal incomes
        incomes.append(d)
        incomes = incomes[-accumulation_period::]
        return sum(incomes) / len(incomes)

    return get_avg
