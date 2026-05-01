from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    data = []

    def get_avg(delta: float) -> float:
        data.append(delta)
        if len(data) > accumulation_period:
            data.pop(0)
        return sum(data) / len(data)

    return get_avg
