import sys

class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file

    def __enter__(self):
        self.output_file = open(self.path_to_file, "w")
        self.original_stdout = sys.stdout
        sys.stdout = self.output_file
        return self

    def __exit__(self, *args):
        sys.stdout = self.original_stdout
        self.output_file.close()
        return False