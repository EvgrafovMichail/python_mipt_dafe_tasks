from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    lastn = []
    sum = 0

    def get_avg(dayprofit):
        nonlocal sum
        if len(lastn) == accumulation_period:
            sum -= lastn[0]
            lastn.pop(0)
        lastn.append(dayprofit)
        sum += dayprofit

        return sum / len(lastn)

    return get_avg
