from typing import Any, Generator, Iterable, Iterator

def takeN(iterator: Iterator, N):
    for _ in range(N):
        try:
            yield next(iterator)
        except StopIteration:
            return
            

def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:

    iterator: Iterator = iter(iterable)
    
    while True:
        chunk = tuple(takeN(iterator, size))
        
        if not chunk:
            return
        
        yield chunk