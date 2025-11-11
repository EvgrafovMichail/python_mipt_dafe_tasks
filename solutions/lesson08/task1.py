from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    n = accumulation_period
    values = []

    def get_avg(value):
        values.append(value)

        if len(values) > n:
            values.pop(0)

        return sum(values) / len(values)

    return get_avg
