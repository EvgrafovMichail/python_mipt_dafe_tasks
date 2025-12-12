import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file

    def __enter__(self):
        self._old_state = sys.stdout
        self._file = open(self._path_to_file, 'w')
        sys.stdout = self._file
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._old_state
        self._file.close()
        return False
