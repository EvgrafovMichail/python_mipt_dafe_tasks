from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    sr = []

    def get_avg(prib):
        sr.append(prib)

        if len(sr) > accumulation_period:
            sr.pop(0)

        return sum(sr) / len(sr)

    return get_avg
