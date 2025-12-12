from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    a = []

    def get_avg(x: float) -> float:
        a.append(x)
        total = 0
        if len(a) <= accumulation_period:
            for i in a:
                total += i
            return total / len(a)

        if len(a) > accumulation_period:
            for i in range(len(a) - accumulation_period, len(a)):
                total += a[i]
            return total / accumulation_period

    return get_avg
