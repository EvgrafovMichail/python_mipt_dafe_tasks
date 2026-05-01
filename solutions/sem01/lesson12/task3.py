import sys


class FileOut:
    _default_stdout = sys.stdout

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file

    def __enter__(self) -> None:
        self._file = open(self._path_to_file, "w")
        sys.stdout = self._file
        return self

    def __exit__(self, *args) -> None:
        sys.stdout = self._default_stdout
        self._file.close()
        return False
