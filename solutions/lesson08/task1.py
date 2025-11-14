from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    pribyl_sredn = []

    def get_avg(m):
        nonlocal pribyl_sredn
        pribyl_sredn.append(m)
        if len(pribyl_sredn) > accumulation_period:
            pribyl_sredn.pop(0)
        return sum(pribyl_sredn) / len(pribyl_sredn)

    return get_avg
