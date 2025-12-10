import sys


class FileOut:
    def __init__(self, path_to_file: str) -> None:
        self.path_to_file = path_to_file

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.file = open(self.path_to_file, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, *args, **kwargs):
        sys.stdout = self.old_stdout
        self.file.close()
