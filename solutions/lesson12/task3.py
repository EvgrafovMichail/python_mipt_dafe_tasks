import sys


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self.path = path_to_file

    def __enter__(self):
        self.old = sys.stdout
        self.file = open(self.path, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.old
        self.file.close()
        return False
