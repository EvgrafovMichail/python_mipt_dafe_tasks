from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    journey = []
    def get_avg(dohod):
        nonlocal journey
        journey.append(dohod)
        if len(journey) > accumulation_period:
            journey.pop(0)
        return sum(journey) / len(journey)
    return get_avg