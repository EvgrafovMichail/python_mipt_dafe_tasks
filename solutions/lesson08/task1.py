from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    val = []

    def get_avg(x: float) -> float:
        nonlocal val
        val.append(x)
        if len(val) > accumulation_period:
            val = val[-accumulation_period:]
        return sum(val) / len(val)

    return get_avg
