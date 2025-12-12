import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file
        self.stdout = None
        self.file = None

    def __enter__(self):
        self.file = open(self.path_to_file, "w")
        self.stdout = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout
        self.file.close()
        self.file = None
        self.stdout = None
        return False
