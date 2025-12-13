import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file
        self._original_stdout = None
        self._file = None

    def __enter__(self):
        self._file = open(self._path_to_file, "w")
        self._original_stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> bool:
        if self._original_stdout is not None:
            sys.stdout = self._original_stdout

        if self._file:
            self._file.close()

        return False
