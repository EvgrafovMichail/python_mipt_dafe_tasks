from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    daily_profits = []
    profit = 0

    def get_avg(day_profit: float) -> float:
        nonlocal daily_profits
        nonlocal profit
        daily_profits.append(day_profit)
        profit += day_profit
        if accumulation_period < len(daily_profits):
            profit -= daily_profits[-(accumulation_period + 1)]
        return profit / min(len(daily_profits), accumulation_period)

    return get_avg
