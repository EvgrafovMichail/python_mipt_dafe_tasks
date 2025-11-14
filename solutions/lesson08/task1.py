from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    values = []

    def get_avg(value_for_day: int) -> float:
        if accumulation_period < 1:
            return 0

        values.append(value_for_day)
        if len(values) > accumulation_period:
            values.pop(0)

        return sum(values) / len(values)

    return get_avg
