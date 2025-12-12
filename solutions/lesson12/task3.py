import sys
from typing import Any, Self, TextIO


class FileOut:
    _prev_stdout: TextIO | None
    _file_path: str
    _file: TextIO | None

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._prev_stdout = None
        self._file_path = path_to_file
        self._file = None

    def __enter__(self) -> Self:
        if self._file:
            raise RuntimeError("File already opened")
        self._prev_stdout = sys.stdout
        self._file = open(self._file_path, "w")
        sys.stdout = self._file
        return self

    def __exit__(self, *_: Any) -> bool:
        if not self._file:
            raise RuntimeError("File not opened")
        sys.stdout = self._prev_stdout
        self._file.close()
        self._file = None
        return False
