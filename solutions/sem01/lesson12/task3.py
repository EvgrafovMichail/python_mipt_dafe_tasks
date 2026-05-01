import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        # ваш код
        self.path_to_file = path_to_file
        self.original_stdout = None
        self.file = None

    # ваш код

    def __enter__(self):
        self._file = open(self.path_to_file, "w")

        self._stdout = sys.stdout
        sys.stdout = self._file
        return self

    def __exit__(self, *args, **kwargs):
        sys.stdout = self._stdout
        self._file.close()
        return False
