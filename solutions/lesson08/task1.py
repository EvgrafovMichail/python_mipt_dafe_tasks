from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    all_days = []

    def get_average(n: int) -> int:
        nonlocal all_days
        all_days.append(n)
        if len(all_days) < accumulation_period:
            return sum(all_days) / len(all_days)
        return sum(all_days[-accumulation_period:]) / accumulation_period

    return get_average
