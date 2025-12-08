import sys
from types import TracebackType
from typing import Optional, Self


class FileOut:
    _path_to_file: str = ""
    _file = None
    _old_stdout = None

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file

    def __enter__(self) -> Self:
        self._old_stdout = sys.stdout
        self._file = open(self._path_to_file, "w")
        sys.stdout = self._file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        if self._old_stdout is not None:
            sys.stdout = self._old_stdout
            self._old_stdout = None

        if self._file is not None:
            self._file.close()
            self._file = None

        return False
