from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    list_of_elements_already_returned = []

    for element in iterable:
        list_of_elements_already_returned.append(element)
        yield element

    iterable_length = len(list_of_elements_already_returned)
    call_number = iterable_length

    if not list_of_elements_already_returned:
        return

    while True:
        call_number += 1
        yield list_of_elements_already_returned[(call_number - 1) % iterable_length]
