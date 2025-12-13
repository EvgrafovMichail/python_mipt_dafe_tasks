from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    prices = []

    def get_avg(price):
        nonlocal prices
        prices.append(price)
        count = 0
        length = len(prices)
        length2 = max(length, accumulation_period)
        for i in range(length - 1, length2 - accumulation_period - 1, -1):
            print(i)
            count += prices[i]
        length = min(length, accumulation_period)
        return count / length

    return get_avg
