from typing import Callable


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    list_of_pluser = list()

    def get_avg(pluser: float):
        nonlocal list_of_pluser
        list_of_pluser.append(pluser)

        if len(list_of_pluser) > accumulation_period:
            list_of_pluser = list_of_pluser[1:]

        return sum(list_of_pluser) / len(list_of_pluser)

    return get_avg
