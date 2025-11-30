from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")

import time
from random import uniform
jitter_time = uniform(0, 0.5)

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
    def wrapper(func: Callable) -> Callable:
        if (retry_amount < 0
                or timeout_max < 0
                or timeout_start < 0
                or backoff_scale < 0):
                raise ValueError
        def inner(*args, **kwargs):
            scale_delay = timeout_start
            for attempt in range(retry_amount):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as exp:
                    if attempt == retry_amount - 1:
                        raise exp
                    
                    if type(exp) not in backoff_triggers:
                        raise exp
                       
                    delay = min(scale_delay, timeout_max)
                    
                    jitter_time = uniform(0, 0.5)
                    time_sleep = delay + jitter_time
                    time.sleep(time_sleep)
                    scale_delay *= backoff_scale
                    
        return inner
    return wrapper

attempts = 0
timeout_max = 4
retry_amount = 4
timeouts = [1, 2, 4, 4]       
@backoff(
        retry_amount=4,
        timeout_start=1,
        timeout_max=10.0,
        backoff_scale=2.0,
        backoff_triggers=(ConnectionError, TimeoutError)
    )
def func():
    global attempts
    attempts += 1
    if attempts < retry_amount:
        raise ConnectionError("Ошибка подключения")
    return "успех"

func()