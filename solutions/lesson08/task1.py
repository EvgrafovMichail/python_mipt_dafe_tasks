from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    alphabet = []

    def get_avg(count: float) -> float:
        alphabet.append(count)

        if len(alphabet) > accumulation_period:
            alphabet.pop(0)

        return sum(alphabet) / len(alphabet)

    return get_avg
