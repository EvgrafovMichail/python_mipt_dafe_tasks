import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.filename = path_to_file
        self.file = None
        self.original_stdout = None

    def __enter__(self):
        self.original_stdout = sys.stdout
        self.file = open(self.filename, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout
        if self.file and not self.file.closed:
            self.file.close()
        return False
