import sys


class FileOut:
    path: str

    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path = path_to_file
        self.stdout = sys.stdout
        self.file = None

    def __enter__(self):
        self.file = open(self.path, "w+")
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        sys.stdout = self.stdout
        return 0
