from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    n = 0
    buhgalter = [0]

    def get_avg(profit: float) -> float:
        nonlocal buhgalter
        nonlocal n
        n += 1
        buhgalter.append(profit)
        if n >= accumulation_period:
            k = accumulation_period
        else:
            k = n
        sum_profit = 0
        for i in range(len(buhgalter) - k, len(buhgalter)):
            sum_profit += buhgalter[i]

        avg = sum_profit / k
        return avg

    return get_avg
