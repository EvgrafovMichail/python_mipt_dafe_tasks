import sys


class FileOut:
    file = None
    path_to_file = None
    original_stdout = None

    def __init__(self, path_to_file: str) -> None:
        self.path_to_file = path_to_file

    def __enter__(self):
        self.file = open(self.path_to_file, "w")
        self.original_stdout = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.original_stdout is not None:
            sys.stdout = self.original_stdout
            self.original_stdout = None

        if self.file:
            self.file.close()
            self.file = None

        return False
