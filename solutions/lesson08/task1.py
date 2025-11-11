from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    money = []

    def profit(new_money: float) -> float:
        money.append(new_money)
        if len(money) > accumulation_period:
            money.pop(0)
        return sum(money) / len(money)

    return profit
