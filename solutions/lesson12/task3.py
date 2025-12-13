import sys
from contextlib import contextmanager

class FileOut:
    path: str
    file: None
    stdout: None
    
    _is_close: bool
    def __init__(
        self,
        path_to_file: str,
    ) -> None:
        self.path = path_to_file
        self._is_close = True
        
    def __enter__(self):
        try:
            self.file = open(self.path, "w")
            self.stdout = sys.stdout
            sys.stdout = self.file
        except Exception as exp:
            if self.stdout is not None:
                sys.stdout = self.stdout
            if self.file is not None:
                self.file.close()
                raise exp
            
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.stdout is not None:
            sys.stdout = self.stdout
        if self.file is not None:
            self.file.close()
        
        return False
        

