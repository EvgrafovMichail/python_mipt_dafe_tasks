from typing import Iterable, Generator, Any, Tuple


def chunked(iterable: Iterable[Any], size: int) -> Generator[Tuple[Any, ...], None, None]:
    if size < 1:
        raise ValueError("Размер чанка (size) должен быть положительным целым числом.")

    chunk = []

    for item in iterable:
        chunk.append(item)

        if len(chunk) == size:
            yield tuple(chunk)
            chunk = []

    if chunk:
        yield tuple(chunk)


if __name__ == "__main__":
    result1 = tuple(chunked([1, 2, 3, 4, 5], 2))
    print(f"chunked([1, 2, 3, 4, 5], 2) -> {result1}")

    result2 = tuple(chunked("abcdef", 3))
    print(f"chunked('abcdef', 3) -> {result2}")

    result3 = tuple(chunked(range(10), 4))
    print(f"chunked(range(10), 4) -> {result3}")

    result4 = tuple(chunked([], 3))
    print(f"chunked([], 3) -> {result4}")
