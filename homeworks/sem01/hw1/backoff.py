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

    if retry_amount < 1 or retry_amount > 100:
        raise ValueError("retry_amount должен быть в диапазоне от 1 до 100")
    
    if timeout_start <= 0 or timeout_start >= 10:
        raise ValueError("timeout_start должен быть в диапазоне (0, 10)")
    
    if timeout_max <= 0 or timeout_max >= 10:
        raise ValueError("timeout_max должен быть в диапазоне (0, 10)")
    
    if backoff_scale <= 0 or backoff_scale >= 10:
        raise ValueError("backoff_scale должен быть в диапазоне (0, 10)")
    
    if not backoff_triggers:
        raise ValueError("backoff_triggers не может быть пустым")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception = None
            current_timeout = timeout_start
            
            for trying in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                   
                    should_retry = any(isinstance(e, trigger) for trigger in backoff_triggers)
                    
                    if not should_retry or trying == retry_amount - 1:

                        raise last_exception
                    
                    jitter = uniform(0, 0.5)
                    total_sleep_time = min(current_timeout + jitter, timeout_max)
                    
                    sleep(total_sleep_time)
                    
                    current_timeout = min(current_timeout * backoff_scale, timeout_max)
            
            raise last_exception
        
        return wrapper
    
    return decorator