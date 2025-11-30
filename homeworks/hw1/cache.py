from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")

class Element:
    key = None
    value = None
    prev = None
    next = None
    def __init__(self, key = 0, value = 0 ):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRU:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError
        
        self.capacity = capacity
        self.cash = {}
        self.head = Element()
        self.tail = Element()    
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def append(self, element: Element):
        element.prev = self.head
        element.next = self.head.next
        
        self.head.next.prev = element
        self.head.next = element
    
    def remove(self, element):
        pass
    
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
    
        
