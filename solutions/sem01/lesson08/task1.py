from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    total_sum = 0
    financial_lst = []

    def get_avg(financial_result: float) -> float:
        nonlocal accumulation_period
        nonlocal total_sum

        financial_lst.append(financial_result)

        if len(financial_lst) > accumulation_period:
            total_sum -= financial_lst[0]
            financial_lst.pop(0)

        total_sum += financial_result
        return total_sum / len(financial_lst)

    return get_avg
