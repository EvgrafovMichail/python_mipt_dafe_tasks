import sys
from typing import IO, Any
from io import FileIO

class FileOut:
    file: FileIO
    path_to_file: str
    stdout: IO
    
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path_to_file = path_to_file
    
    def __enter__(self):
        self.file = open(self.path_to_file, 'w')
        
        self.stdout = sys.stdout
        sys.stdout = self.file
        return self
    
    def __exit__(self, *_: Any):
        sys.stdout = self.stdout
        self.file.close()
        return False


with FileOut('text.txt') as filem:
    print("aaaa")
    
