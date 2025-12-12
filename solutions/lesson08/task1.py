from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    daily_profits = []

    def get_avg(profit: float) -> float:
        daily_profits.append(profit)
        if len(daily_profits) < accumulation_period:
            return sum(daily_profits) / len(daily_profits)
        return sum(daily_profits[-accumulation_period:]) / accumulation_period

    return get_avg
