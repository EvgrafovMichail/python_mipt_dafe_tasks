import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self._path_to_file = path_to_file
        self._main_stdout = None
        self._file = None

    def __enter__(self) -> "FileOut":
        self._main_stdout = sys.stdout
        self._file = open(self._path_to_file, 'w')
        sys.stdout = self._file
        return self
    
    def __exit__(self, *_) -> bool:
        sys.stdout = self._main_stdout
        if self._file:
            self._file.close()
            self._file = None
        return False