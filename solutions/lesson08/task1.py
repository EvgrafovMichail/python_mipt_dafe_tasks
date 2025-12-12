from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    amount_lst: list[float] = []

    def get_avg(amount: float) -> float:
        nonlocal amount_lst
        amount_lst.append(amount)
        if len(amount_lst) < accumulation_period:
            return sum(amount_lst) / len(amount_lst)
        else:
            end_index = -1 - accumulation_period
            return sum(amount_lst[-1:end_index:-1]) / accumulation_period

    return get_avg
