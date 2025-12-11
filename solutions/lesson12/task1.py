from typing import Any, Generator, Iterable

def chunked(iterable: Iterable, size: int) -> Generator[tuple[Any], None, None]:
    # ваш код
    block = []
    for element in iterable:
        
        block.append(element)
        
        if len(block) == size:
            
            yield (tuple(block))
            block = []
    
    if block:
        
        yield tuple(block)