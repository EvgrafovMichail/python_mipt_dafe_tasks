import sys
from typing import Any, Self


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path = path_to_file
        self._original_stdout = sys.stdout
        self._file = None

    def __enter__(self) -> Self:
        self._file = open(self._path, "w")
        sys.stdout = self._file
        return self

    def __exit__(self, *_: Any) -> bool:
        if self._file is not None and not self._file.closed:
            self._file.flush()
            sys.stdout = self._original_stdout
            self._file.close()
        return False
