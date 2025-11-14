from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    profit = []

    def wrapper(n: float) -> float:
        profit.append(n)
        if len(profit) > accumulation_period:
            del profit[0]
        return sum(profit) / len(profit)

    return wrapper
