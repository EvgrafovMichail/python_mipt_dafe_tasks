import typing


def make_averager(accumulation_period: int) -> typing.Callable[[float], float]:
    sum_change = []

    def get_avg(value: float):
        nonlocal sum_change
        sum_change.append(value)
        if len(sum_change) > accumulation_period:
            sum_change.pop(0)
        avg = sum(sum_change) / len(sum_change)
        return avg

    return get_avg
