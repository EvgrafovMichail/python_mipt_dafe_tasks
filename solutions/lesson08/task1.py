import math
from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    last_m_days = [0.0] * accumulation_period
    days = 0
    sum_days = 0
    is_n_days = 0

    def get_avg(day_result):
        nonlocal last_m_days
        nonlocal days
        nonlocal sum_days
        nonlocal is_n_days

        sum_days -= last_m_days[days]
        last_m_days[days] = day_result
        sum_days += day_result
        days += 1
        if days == accumulation_period and is_n_days == 0:
            is_n_days = 1
        days = days % accumulation_period

        if is_n_days == 0:
            return sum_days / days
        else:
            return sum_days / accumulation_period

    return get_avg


pass
get_avg = make_averager(2)
assert math.isclose(get_avg(1), 1)
assert math.isclose(get_avg(2), 1.5)
assert math.isclose(get_avg(3), 2.5)
assert math.isclose(get_avg(-3), 0)
assert math.isclose(get_avg(5), 1)
assert math.isclose(get_avg(5), 5)

get_avg = make_averager(5)

assert math.isclose(get_avg(1), 1)
assert math.isclose(get_avg(2), 1.5)
assert math.isclose(get_avg(3), 2)
assert math.isclose(get_avg(4), 2.5)
assert math.isclose(get_avg(5), 3)
assert math.isclose(get_avg(-5), 1.8)
assert math.isclose(get_avg(-7), 0)
assert math.isclose(get_avg(-2), -1)
