from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.know_args = {}

        self.head = node()
        self.tail = node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, args):
        if args in self.know_args:
            get_node = self.know_args[args]
            self.delete(get_node)
            self.add(get_node)
            return get_node.value
        else:
            return None

    def put(self, ans, args):
        if args in self.know_args:
            put_node = self.know_args[args]
            put_node.value = ans
            self.delete(put_node)
            self.add(put_node)
        else:
            if len(self.know_args) >= self.capacity:
                last_node = self.tail.prev
                self.delete(last_node)
                self.know_args.pop(last_node.args)

            put_node = node(args, ans)
            self.know_args[args] = put_node
            self.add(put_node)


class node:
    def __init__(self, args=None, value=None):
        self.value = value
        self.args = args
        self.next = None
        self.prev = None


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
        rounded_capacity = round(capacity)
    except Exception as exc:
        raise exc

    if rounded_capacity < 1:
        raise ValueError

    def decorator(func):
        lru_local = LRU(rounded_capacity)

        def wrapper(*args, **kwargs):
            arguments = (args, tuple(sorted(kwargs.items())))
            if arguments in lru_local.know_args:
                return lru_local.get(arguments)
            else:
                ans = func(*args, **kwargs)
                lru_local.put(ans, arguments)
                return ans

        return wrapper

    return decorator
