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

    if retry_amount <= 0 or retry_amount > 100:
        raise ValueError("retry_amount должен быть положительным числом от 1 до 100")
    
    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError("timeout_start должен быть положительным числом в диапазоне (0, 10)")
    
    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError("timeout_max должен быть положительным числом в диапазоне (0, 10)")
    
    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError("backoff_scale должен быть положительным числом в диапазоне (0, 10)")
    
    if not backoff_triggers or not all(issubclass(trig, Exception) for trig in backoff_triggers):
        raise ValueError("backoff_triggers должен быть непустым кортежем типов исключений")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception = None
            current_timeout = timeout_start
            
            for attempt in range(retry_amount + 1):
                try:
                    if attempt > 0:
                        jitter = uniform(0, 0.5)
                        sleep_time = min(current_timeout + jitter, timeout_max + jitter)
                        sleep(sleep_time)
                        current_timeout = min(current_timeout * backoff_scale, timeout_max)
                    
                    return func(*args, **kwargs)
                    
                except backoff_triggers as e:
                    last_exception = e
                    
                    if attempt == retry_amount:
                        raise last_exception
        return wrapper
    return decorator
