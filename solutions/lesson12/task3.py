import sys
from builtins import bool
from types import TracebackType
from typing import Optional


class FileOut:
    __path: str

    def __init__(self, path_to_file: str) -> None:
        self.__path = path_to_file

    def __enter__(self) -> "FileOut":
        self.__file = open(self.__path, "w")
        self.__stdout = sys.stdout
        sys.stdout = self.__file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        sys.stdout = self.__stdout
        if exc_type is None:
            self.__file.close()
        return False
