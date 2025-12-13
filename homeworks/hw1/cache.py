from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


@dataclass
class Node:
    key: Any = None
    value: Any = None

    prev: Any = None
    next: Any = None


class CacheContainer:
    table: dict
    head: Node
    tail: Node

    capacity: int
    size: int

    def __init__(self, capacity):
        self.table = {}

        self.capacity = capacity
        self.size = 0

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def __add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1
        self.table[node.key] = node

    def __remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
        self.table.pop(node.key)

    def place(self, node: Node):
        self.__update(node)

        if self.size > self.capacity:
            self.__remove(self.tail.prev)

    def __update(self, node: Node):
        if node.key in self.table:
            self.__remove(node)

        self.__add(node)

    def get(self, key: Any):
        if key not in self.table:
            return None

        node = self.table[key]
        self.__update(node)

        return node.value


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

    try:
        capacity = round(capacity)
    except TypeError:
        raise TypeError("capacity shoud support round()")

    if capacity < 1:
        raise ValueError("capacity shoud be not less than 1")

    def decorator(function):
        cache = CacheContainer(capacity)

        @wraps(function)
        def wrapper(*vargs: ..., **kwargs: ...) -> R:
            args = (*vargs, *(sorted(kwargs.items())))

            result = cache.get(args)

            if result is None:
                result = function(*vargs, **kwargs)

                cache.place(Node(key=args, value=result))

            return result

        return wrapper

    return decorator
