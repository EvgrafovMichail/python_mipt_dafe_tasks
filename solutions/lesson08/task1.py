from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    profits_by_period = [0] * accumulation_period
    count = 0

    def get_avg(day_profit: float) -> float:
        nonlocal profits_by_period
        nonlocal count
        count += 1
        if count <= accumulation_period:
            profits_by_period[count - 1] = day_profit
            return sum(profits_by_period) / count
        else:
            for i in range(1, len(profits_by_period)):
                profits_by_period[i - 1] = profits_by_period[i]
            profits_by_period[-1] = day_profit
            return sum(profits_by_period) / accumulation_period

    return get_avg
