from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    daily_profits = [0.0] * accumulation_period
    total = 0.0
    count = 0
    index = 0

    def get_wg(daily_profit: float) -> float:
        nonlocal total, count, index

        if count < accumulation_period:
            total += daily_profit
            daily_profits[index] = daily_profit
            count += 1
        else:
            total = total - daily_profits[index] + daily_profit
            daily_profits[index] = daily_profit

        index = (index + 1) % accumulation_period
        return total / count

    return get_wg
