import sys
from types import TracebackType
from typing import Optional


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self._path_to_file = path_to_file
        self._original_stdout = None
        self._file = None

    def __enter__(self) -> "FileOut":
        self._file = open(self._path_to_file, "w")
        self._original_stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        sys.stdout = self._original_stdout

        if self._file and not self._file.closed:
            self._file.close()

        return False
