from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    ans = []

    def get_avg(value):
        ans.append(value)

        if len(ans) > accumulation_period:
            ans.pop(0)

        return sum(ans) / len(ans)

    return get_avg
