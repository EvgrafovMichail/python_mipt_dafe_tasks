import sys
from typing import Optional, Self
from types import TracebackType

class FileOut:
    def __init__(self, path_to_file: str,) -> None:
        self._path_to_file = path_to_file
        self._orig_stdout = None
        self._outfile = None
    
    def __enter__(self) -> Self:
        self._orig_stdout = sys.stdout
        self._outfile = open(self._path_to_file, 'w')
        sys.stdout = self._outfile
        return self
    
    def __exit__(self, 
                 exc_type: Optional[type[BaseException]], 
                 exc_val: Optional[BaseException], 
                 exc_tb: Optional[TracebackType]) -> bool:
        self._restore_stdout()
        self._close_file()
        return False
    
    def _restore_stdout(self) -> None:
        if self._orig_stdout is not None:
            sys.stdout = self._orig_stdout
            self._orig_stdout = None
    
    def _close_file(self) -> None:
        if self._outfile and not self._outfile.closed:
            self._outfile.close()
        self._outfile = None