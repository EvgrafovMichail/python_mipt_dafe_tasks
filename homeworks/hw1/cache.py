from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.begin = None
        self.end = None

    def add_to_end(self, node: Node):
        if self.end is not None:
            self.end.next = node
            node.prev = self.end
            self.end = node
        else:
            self.end = node
            self.begin = node

    def delete_begin(self):
        if self.begin.next is None:
            self.begin = None
            self.end = None
        else:
            if self.begin.next is not None:
                self.begin.next.prev = None
                self.begin = self.begin.next
            else:
                self.begin = None
                self.end = None

    def move_to_end(self, node: Node):
        if node.next is not None:
            node.next.prev = node.prev

            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.begin = node.next
            node.prev = self.end
            self.end.next = node
            node.next = None
            self.end = node


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
    # создание ошибок
    try:
        capacity = round(capacity)
    except Exception:
        raise TypeError("Недопустимый тип размера")
    else:
        if capacity < 1:
            raise ValueError("Недопустимый размер")

    def wrapper(func):
        keys_to_obj = {}
        priorities = Deque()

        def func_with_cache(*args, **kwargs):
            # формируем кортеж с набором аргументов

            arguments = (args, tuple(sorted(kwargs.items())))
            """for i in range(len(args)):
                arguments[(func.__code__.co_varnames)[i]]=args[i] #получение позиционных аргументов
            
            for var in func.__code__.co_varnames[len(args):func.__code__.co_argcount]:
                arguments[var]=kwargs[var]                          #получение ключевых аргументов
            arguments=tuple(arguments.items())"""

            if arguments in keys_to_obj:
                priorities.move_to_end(keys_to_obj[arguments])

                return keys_to_obj[arguments].data
            else:
                result = func(*args, **kwargs)
                obj = Node(arguments, result)

                if len(keys_to_obj) == capacity:
                    keys_to_obj.pop(priorities.begin.key)
                    priorities.delete_begin()

                    priorities.add_to_end(obj)
                    keys_to_obj[arguments] = obj
                else:
                    keys_to_obj[arguments] = obj
                    priorities.add_to_end(obj)

                return result

        return func_with_cache

    return wrapper
