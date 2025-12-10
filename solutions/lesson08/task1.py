from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    data = list[float]()

    def get_avg(day_income: float) -> float:
        data.append(day_income)

        if accumulation_period > (data_len := len(data)):
            return sum(data) / data_len

        return sum(data[-i] for i in range(1, accumulation_period + 1)) / accumulation_period

    return get_avg
