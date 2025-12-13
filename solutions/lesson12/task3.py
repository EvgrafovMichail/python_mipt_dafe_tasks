import sys


class FileOut:
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path = path_to_file
        self.file = None
        self.old_text = None

    def __enter__(self):
        self.file = open(self.path, "w")
        self.old_text = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(self, *_):
        sys.stdout = self.old_text
        self.file.close()
        return False
