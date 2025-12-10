import sys
from types import TracebackType
from typing import Optional, Self


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self.path_to_file = path_to_file
        self.file = None
        self.original_stdout = None

    def __enter__(self) -> Self:
        self.original_stdout = sys.stdout
        self.file = open(self.path_to_file, "w", encoding="utf-8")
        sys.stdout = self.file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        if self.original_stdout is not None:
            sys.stdout = self.original_stdout
        if self.file is not None and not self.file.closed:
            self.file.close()
        return False
