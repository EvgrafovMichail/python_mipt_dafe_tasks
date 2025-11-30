from typing import (
    Any,
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    Args:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """

    # ваш код
    class MyKnot:
        def __init__(self, key: Any, result: Any, next=None, prev=None):
            self.key = key
            self.result = result
            self.prev = prev
            self.next = next

    class MyList:
        def __init__(self, capacity_int: int):
            self.capacity_int = capacity_int
            self.cashe = {}

            # Создаем фиктивные head и tail
            self.head = MyKnot(None, None)
            self.tail = MyKnot(None, None)
            self.head.next = self.tail
            self.tail.prev = self.head

        def move(self, key: Any):
            # Перемещает узел в начало (после head)
            node = self.cashe[key]

            # Удаляем узел из текущей позиции
            node.prev.next = node.next
            node.next.prev = node.prev

            # Вставляем после head
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        def adding(self, key: Any, result: Any):
            # Добавляет новый узел в начало
            # Создаем новый узел после head
            new_node = MyKnot(key, result, self.head.next, self.head)
            self.head.next.prev = new_node
            self.head.next = new_node
            self.cashe[key] = new_node

            # Проверяем capacity
            if len(self.cashe) > self.capacity_int:
                # Удаляем самый старый узел (перед tail)
                to_remove = self.tail.prev
                to_remove.prev.next = self.tail
                self.tail.prev = to_remove.prev
                del self.cashe[to_remove.key]

        def get(self, key: Any):
            # Получает значение по ключу
            if key in self.cashe:
                self.move(key)
                return self.cashe[key].result
            else:
                return None

    # Валидация capacity
    try:
        capacity_int = round(capacity)
    except (TypeError, ValueError):
        raise TypeError("capacity must be convertible to int")

    if capacity_int < 1:
        raise ValueError("capacity must be at least 1")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = MyList(capacity_int)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))

            result = cache.get(key)

            if result is not None:
                return result

            result = func(*args, **kwargs)
            cache.adding(key, result)

            return result

        return wrapper

    return decorator
