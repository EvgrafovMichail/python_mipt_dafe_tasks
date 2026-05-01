from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    # ваш код
    chunk = []
    append_to_chunk = chunk.append
    for item in iterable:
        append_to_chunk(item)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk = []
            append_to_chunk = chunk.append

    if chunk:
        yield tuple(chunk)
