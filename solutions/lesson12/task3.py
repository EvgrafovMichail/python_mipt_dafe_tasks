import sys


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self._path_to_file: str = path_to_file

    def __enter__(self) -> "FileOut":
        self._orig_stdout = sys.stdout
        self._file = open(self._path_to_file, "w")
        sys.stdout = self._file
        return self

    def __exit__(self, *_) -> bool:
        self._file.close()
        sys.stdout = self._orig_stdout
        return False
