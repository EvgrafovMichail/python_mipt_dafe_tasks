import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path = path_to_file

    def __enter__(self):
        self.file = open(self.path, "w")
        self.stdout = sys.stdout
        sys.stdout = self.file

        return self

    def __exit__(self, *_):
        sys.stdout = self.stdout
        self.file.close()
