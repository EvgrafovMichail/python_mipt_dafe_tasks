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
    backoff_triggers: tuple[type[Exception], ...] = (Exception,),
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

    # Проверяем, что все параметры правильные
    if retry_amount <= 0 or retry_amount > 100:
        raise ValueError("retry_amount должен быть от 1 до 100")

    if timeout_start <= 0 or timeout_start > 10:
        raise ValueError("timeout_start должен быть от 0 до 10")

    if timeout_max <= 0 or timeout_max > 10:
        raise ValueError("timeout_max должен быть от 0 до 10")

    if backoff_scale <= 0 or backoff_scale > 10:
        raise ValueError("backoff_scale должен быть от 0 до 10")

    # Это сам декоратор
    def decorator(func: Callable[P, R]) -> Callable[P, R]:

        # Это обертка вокруг функции
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Начинаем с начального времени ожидания
            current_timeout = timeout_start
            # Считаем сколько попыток осталось (включая первую)
            attempts_left = retry_amount

            # Пока есть попытки - пробуем выполнить функцию
            while attempts_left > 0:
                try:
                    # Пытаемся выполнить функцию
                    return func(*args, **kwargs)

                except backoff_triggers as error:
                    # Уменьшаем количество оставшихся попыток
                    attempts_left -= 1

                    # Если попытки закончились - выбрасываем ошибку
                    if attempts_left == 0:
                        raise error

                    # Добавляем случайное число чтобы разные процессы ждали разное время
                    random_jitter = uniform(0, 0.5)
                    # Вычисляем сколько ждать (не больше максимума)
                    sleep_time = min(current_timeout + random_jitter, timeout_max)

                    # Ждем
                    sleep(sleep_time)

                    # Увеличиваем время ожидания для следующей попытки
                    current_timeout = min(current_timeout * backoff_scale, timeout_max)

                except Exception as error:
                    # Если ошибка не в backoff_triggers - сразу пробрасываем
                    raise error

        return wrapper

    return decorator