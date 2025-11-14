from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    investment_history = []

    def get_avg(income):
        investment_history.append(income)

        if len(investment_history) > accumulation_period:
            investment_history.pop(0)

        return sum(investment_history) / len(investment_history)

    return get_avg

    pass
