import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._file = open(self.path_to_file, 'w')
        sys.stdout = self._file
        return self
    def __exit__(self, *_):
        sys.stdout = self._original_stdout
        if self._file:
            self._file.close()
        return False