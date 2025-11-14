from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    days = 0
    all_money = []

    def get_avg(money: float) -> float:
        nonlocal days
        nonlocal all_money

        if days < accumulation_period:
            all_money.append(money)
            days += 1
            return sum(all_money) / days

        else:
            all_money.append(money)
            del all_money[0]
            return sum(all_money) / accumulation_period

    return get_avg
