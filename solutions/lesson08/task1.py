from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    # ваш код

    def decorator(func):
        values = []

        def wrapper(pribyl: float):
            values.append(pribyl)
            if len(values) > accumulation_period:
                values.pop(0)
            count = len(values)
            total_sum = sum(values)
            return total_sum / count

        return wrapper

    def get_avg(pribyl: float):
        return pribyl

    get_avg = decorator(get_avg)

    return get_avg

    pass
