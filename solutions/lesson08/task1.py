from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    history_money = []

    def get_avg(profit):
        history_money.append(profit)
        if len(history_money) > accumulation_period:
            history_money.pop(0)
        return sum(history_money) / len(history_money)

    return get_avg
