from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    values = []

    def get_avg(value: float) -> float:
        values.append(value)
        if len(values) > accumulation_period:
            values.pop(0)
        return sum(values) / len(values)

    return get_avg
