from typing import Any, Generator, Iterable


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    
    iterator = iter(iterable)
    lst_el = []
    flag = True
    index = 0
    if not iterable:
        return 0
    while True:
        if flag:
            try:
                el = next(iterator)
                lst_el.append(el)
                yield el
                continue
            except StopIteration:
                flag = False
                
        yield lst_el[index % len(lst_el)]
        index += 1
            
#circle_gen = circle('')

#for i in range(5):
#    print(next(circle_gen))
# a
# b
# c
# a
# b        
        
