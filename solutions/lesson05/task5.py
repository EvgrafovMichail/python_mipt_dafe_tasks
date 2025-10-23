def reg_validator(reg_expr: str, text: str) -> bool:
    i, j = 0, 0
    
    while i < len(text) and j < len(reg_expr):
        
        if reg_expr[j]== 'd':

            if not text[i].isdigit():
                return False
           
            while i < len(text) and text[i].isdigit():
                i += 1
            j += 1
            
        elif reg_expr[j]== 'w':

            if not text[i].isalpha():
                return False
            
            while i < len(text) and text[i].isalpha():
                i += 1
            j += 1
            
        elif reg_expr[j]== 's':

            if not (text[i].isalpha() or text[i].isdigit()):
                return False
            
            while i < len(text) and (text[i].isalpha() or text[i].isdigit()):
                i += 1
            j += 1
            
        else:

            if text[i] != reg_expr[j]:
                return False
            i += 1
            j += 1
    
    return i == len(text) and j == len(reg_expr)


