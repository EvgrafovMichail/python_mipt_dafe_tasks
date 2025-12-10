import sys
from typing import Optional, Self, TextIO


class FileOut:
    path_to_file: str
    stdout: Optional[TextIO]
    file: Optional[TextIO]

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file
        self.stdout = None
        self.file = None

    def __enter__(self) -> Self:
        self.file = open(self.path_to_file, "w")
        self.stdout = sys.stdout
        sys.stdout = self.file

        return self

    def __exit__(self, *_) -> bool:
        sys.stdout = self.stdout
        if self.file:
            self.file.close()

        return False
