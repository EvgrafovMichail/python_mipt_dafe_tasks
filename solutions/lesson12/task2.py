from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    elements = []
    for elem in iterable:
        elements.append(elem)
        yield elem

    # Если iterable был пуст
    if not elements:
        return

    # Бесконечный цикл: на каждом круге создаём новый итератор по кэшированным элементам
    while True:
        for elem in elements:
            yield elem