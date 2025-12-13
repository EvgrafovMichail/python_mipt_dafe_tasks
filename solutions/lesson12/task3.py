import sys
sys.version


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.filepath = path_to_file
        self.file = None
        self.oldout = None

    def __enter__(self):
        self.oldout = sys.stdout
        self.file = open(self.filepath, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, *args):
        sys.stdout = self.oldout
        if self.file:
            self.file.close()
        return False  # False - исключения не подавляются
