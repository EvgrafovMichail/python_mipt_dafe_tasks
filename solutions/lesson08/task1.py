from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    period = accumulation_period
    prices = []

    def get_avg(price):
        nonlocal prices
        prices.append(price)
        count = 0
        _len = len(prices)
        for i in range(_len - 1, (_len - period - 1 if _len > period else -1), -1):
            count += prices[i]
        return count / (_len if _len <= period else period)

    return get_avg
