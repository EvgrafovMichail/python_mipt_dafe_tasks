from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    income = []
    sum = 0

    def get_avg(n: int):
        nonlocal income, sum
        income.append(n)

        sum += n
        if len(income) > accumulation_period:
            sum -= income[len(income) - 1 - accumulation_period]
            return sum / accumulation_period

        return sum / len(income)

    return get_avg
