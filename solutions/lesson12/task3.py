import sys
from typing import Any


class FileOut:
    old_std_out: str=''
    
    def __init__(
        self,
        path_to_file: str,
    ) ->None:
        self.path_to_file = path_to_file
    def __enter__(self):
        self.old_std_out = sys.stdout
        self.file = open(self.path_to_file, 'w')
        sys.stdout = self.file
        return self
    def __exit__(self, *_: Any):
        sys.stdout = self.old_std_out
        self.file.close()
        return False
    # ваш код
