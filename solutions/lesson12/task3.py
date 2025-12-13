import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file
        self.file = None
        self.stdout = None

    def __enter__(self):
        self.file = open(self.path_to_file, "w")
        self.stdout = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(self, *args):
        if self.file:
            self.file.close()
        sys.stdout = self.stdout
        return False
