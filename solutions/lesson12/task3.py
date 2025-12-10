import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file

    def __enter__(self):
        self._file = open(self.path_to_file, "w")
        self._stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(self, *_):
        sys.stdout = self._stdout
        self._file.close()
        return False
