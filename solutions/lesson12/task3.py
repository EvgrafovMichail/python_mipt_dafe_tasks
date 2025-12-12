import sys
from typing import Any, Self


class FileOut:
    _path: str
    _file: Any
    _stdout: Any

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path = path_to_file

    def __enter__(self) -> Self:
        return self._open_file()

    def _open_file(self) -> Self:
        self._file = open(self._path, "w")
        self._stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(self, *_: Any) -> bool:
        self._close_file()
        return False

    def _close_file(self) -> None:
        sys.stdout = self._stdout
        self._file.close()
