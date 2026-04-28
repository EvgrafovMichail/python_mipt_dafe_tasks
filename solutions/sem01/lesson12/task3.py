import sys
from types import TracebackType
from typing import Optional


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file

    def __enter__(self) -> "FileOut":
        self._file = open(self._path_to_file, "w")
        self._stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        sys.stdout = self._stdout
        self._file.close()
        return False
