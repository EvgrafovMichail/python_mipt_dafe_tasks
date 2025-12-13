from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    lst = []
    sum_period = 0

    def get_avg(profit: int) -> int:
        nonlocal sum_period
        lst.append(profit)
        sum_period += profit

        if len(lst) > accumulation_period:
            extra = lst.pop(0)
            sum_period -= extra

        return sum_period / len(lst)

    return get_avg
