import sys


class FileOut:
    def __init__(self, path_to_file: str):
        self.path = path_to_file
        self.file = None
        self.old_stdout = None
    
    def __enter__(self):
        self.old_stdout = sys.stdout
        self.file = open(self.path, 'w')
        sys.stdout = self.file
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_stdout
        if self.file:
            self.file.close()
        return False