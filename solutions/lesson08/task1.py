from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    queue = [0] * accumulation_period
    back_position = 0
    accumulator = 0
    count = 0

    def get_avg(value: float) -> float:
        nonlocal accumulator
        nonlocal back_position
        nonlocal count

        count = min(count + 1, accumulation_period)

        back_position = (back_position + 1) % accumulation_period

        accumulator += value - queue[back_position]

        queue[back_position] = value

        return accumulator / count

    return get_avg
