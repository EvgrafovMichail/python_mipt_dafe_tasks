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
        self.prev: Element = None #linking on the prev element
        self.next: Element = None #linking on the next element
class LRU:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError
        
        self.capacity = capacity
        self.cash = {}
        self.head = Element()
        self.tail = Element()    
        self.head.next = self.tail #head(next)<->_<->tail(prev)
        self.tail.prev = self.head
        
    def _append(self, element: Element):
        element.prev = self.head #head->A
        element.next = self.head.next #head->A->taile
        
        self.head.next.prev = element #head<->A->tail
        self.head.next = element #head<->A<->tail
        
    def _remove(self, element): #поля prev и next не None
        if element.prev: #Если не head
            element.prev.next = element.next
        if element.next: #Если не tail
            element.next.prev = element.prev
    
    def _remove_last(self):
        prev_tail = self.tail.prev
        prev_tail.prev.next = self.tail
        
    def _move_to_head(self, element):
        self._remove(element)
        self._append(element)
    
    def _get(self, key):
        if key not in self.cash:
            return None
        
        self._move_to_head(self.cash[key])
        return self.cash[key]
    
    def put_in_cash(self, key, value):
        new = Element(key, value)
        self.cash[key] = new
        self._append(new)

        if self.capacity < len(self.cash):
            self._append(new)
            self._remove_last()
            item_del = self.cash.popitem()
            
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
    def wrapper(func: Callable):
        cash = LRU(round(capacity))
        def inner(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            res = func(*args, **kwargs)
            if cash._get(key) is not None:
                cash._move_to_head(Element(key, res))
            else:
                cash.put_in_cash(key, res)
            
            return res
        return inner
    return wrapper


@lru_cache(capacity=2)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")

    return greeting


print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
        
