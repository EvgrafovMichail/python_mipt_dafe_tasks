import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.file_path = path_to_file

    def __enter__(self):
        self.original_stdout = sys.stdout
        self.file = open(self.file_path, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout
        self.file.close()
        if exc_type is not None:
            raise exc_value
