import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    # запоминаем стаситстику и объявляем декоратор
    def decorator(func: Callable):
        # далле работа чистого декоратора, создаем обертку

        def wrapper(*args, **kwargs):
            # считеем время
            start = time.time()
            out = func(*args, **kwargs)
            delta_time = time.time() - start

            # задаем имя функции
            func_name = func.__name__

            # проверяем есть ли фунция в статистике и обновляем значиения

            if func_name not in statistics:
                statistics[func_name] = [delta_time, 1]
            else:
                time_avg, call_counter = statistics[func_name]
                new_call_counter = call_counter + 1
                # считаем среднее время сразу
                new_time_avg = (time_avg * (new_call_counter - 1) + delta_time) / new_call_counter
                statistics[func_name] = [new_time_avg, new_call_counter]
            return out

        # чтобы при обращении func.__name__ не выдало wrapper
        wrapper.__name__ = func.__name__
        return wrapper

    return decorator
