from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Priorities:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, data):
        new = Node(data)
        new.next = self.head.next
        new.prev = self.head
        self.head.next = new
        self.head.next.prev = new
        return new

    def remove_last(self):
        last = self.tail.prev
        return last.data

    def set_lowest_priority(self, ref):
        first = self.head.next
        prev = ref.prev
        next = ref.next
        if prev and next:
            prev.next, next.prev = next, prev
        ref.prev = self.head
        ref.next = first
        first.prev = ref


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
    del_priorities = Priorities()
    cache = {}

    def decorator(func):
        def wrapper(*args):
            nonlocal cache, del_priorities
            if (args) in cache:
                curr_priority = cache[args][1]
                res = cache[args][0]
                del_priorities.set_lowest_priority(curr_priority)
                return res
            else:
                res = func(*args)
                if len(cache) < capacity:
                    cache[args] = [res, del_priorities.add(args)]
                    return res
                else:
                    cache.pop(del_priorities.remove_last())
                    cache[args] = [res, del_priorities.add(args)]
                    return res

        return wrapper

    return decorator
