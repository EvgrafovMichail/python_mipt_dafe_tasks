from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    ihzbudetlietorabotat = []

    for i in iterable:
        ihzbudetlietorabotat.append(i)

    if not ihzbudetlietorabotat:
        return

    N = len(ihzbudetlietorabotat)
    i = 0

    while True:
        index = i % N

        yield ihzbudetlietorabotat[index]

        i += 1
