from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для повторных запусков функций.

    Args:
        retry_amount: максимальное количество попыток выполнения функции;
        timeout_start: начальное время ожидания перед первой повторной попыткой (в секундах);
        timeout_max: максимальное время ожидания между попытками (в секундах);
        backoff_scale: множитель, на который увеличивается задержка после каждой неудачной попытки;
        backoff_triggers: кортеж типов исключений, при которых нужно выполнить повторный вызов.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        ValueError, если были переданы невозможные аргументы.
    """
    def deco(func):
        def wrapper(*args, **kwargs):
            if (retry_amount > 0) and (timeout_start > 0) and (timeout_max > 0) and \
                (backoff_scale > 0):
                timeout_start1 = timeout_start
                counter = 1
                last_exception = None

                while counter <= retry_amount:
                    try:
                        res = func(*args, **kwargs)
                        return res

                    except Exception as exception1:
                        counter += 1

                        jitter_time = uniform(0, 0.5)

                        if timeout_start1 < timeout_max:
                            current_timeout = timeout_start1 + jitter_time
                            timeout_start1 *= backoff_scale

                        else:
                            current_timeout = timeout_max + jitter_time

                        last_exception = exception1

                        if any(isinstance(exception1, trigger) for trigger in backoff_triggers):
                            sleep(current_timeout)
                            continue
                        else:
                            raise exception1
                raise last_exception

            else:
                raise ValueError()
        return wrapper
    return deco
