from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    bigmoney = []
    maxlen = accumulation_period

    def inner_func(money):
        nonlocal bigmoney, maxlen
        if len(bigmoney) >= maxlen:
            bigmoney.pop(0)
        bigmoney.append(money)
        return sum(bigmoney) / len(bigmoney)

    return inner_func
