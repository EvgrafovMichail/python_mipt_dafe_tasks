import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path = path_to_file
        self._stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._path, "w")
        sys.stdout = self._file
        return self

    def __exit__(self, *args, **kwargs):
        sys.stdout = self._stdout
        self._file.close()
