import sys


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self._path_to_file: str = path_to_file

    def __enter__(self) -> "FileOut":
        self._orig_stdout = sys.stdout
        sys.stdout = open(self._path_to_file, "w")
        return self

    def __exit__(self, *args) -> bool:
        sys.stdout.close()
        sys.stdout = self._orig_stdout
        return False
