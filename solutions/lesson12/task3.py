import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path = path_to_file
        self.stdout = sys.stdout

    def __enter__(self):
        sys.stdout = open(self.path, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = sys.stdout
        sys.stdout = self.stdout
        file.close()
