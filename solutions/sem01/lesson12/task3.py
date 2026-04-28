import sys
from types import TracebackType
from typing import Optional, Self


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self._path_to_file = path_to_file
        self._stdout = None
        self._file = None

    def __enter__(self) -> Self:
        self._stdout = sys.stdout
        self._file = open(self._path_to_file, "w", encoding="utf-8")
        sys.stdout = self._file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        if self._stdout is not None:
            sys.stdout = self._stdout
            self._stdout = None

        if self._file is not None:
            self._file.close()
            self._file = None

        return False
