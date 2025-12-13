from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def example_function(x: int) -> int:
    return x * 2


def main() -> None:
    example_function(5)


if __name__ == "__main__":
    main()