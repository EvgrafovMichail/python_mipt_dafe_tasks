import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.file_path = path_to_file
        self.file = None
        self.old_stdout = None

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.file = open(self.file_path, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_stdout

        if self.file:
            try:
                self.file.close()
            except Exception:
                pass
        return False
