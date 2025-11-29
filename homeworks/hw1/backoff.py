from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)
from functools import wraps

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
    if (retry_amount <= 0 or timeout_max <= 0 or timeout_start <= 0 
     or backoff_scale <= 0):
        raise ValueError("Detected negative number, use positive numbers for decorator")
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kargs):
            delay = timeout_start
            for i in range(retry_amount + 1):
                try:
                    return func(*args,**kargs)
                except backoff_triggers as exc:
                    if i == retry_amount + 1:
                        raise
                    delay_amount = min(timeout_max, delay ) + uniform(0, 0.5)
                    sleep(delay_amount)
                    delay *= backoff_scale
                except Exception:
                    raise
        return wrapper
    return decorator         

