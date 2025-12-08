from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    item_list = []
    for item in iterable:
        item_list.append(item)

        if len(item_list) >= 1e6:  # Condition to avoid infinite loop
            break

    if not item_list:
        return

    i = 0
    while True:
        yield item_list[i % len(item_list)]
        i += 1
