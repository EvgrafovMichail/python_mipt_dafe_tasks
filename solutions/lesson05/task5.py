def reg_validator(reg_expr: str, text: str) -> bool:  
    i = 0
    r = 0
    
    while r < len(reg_expr) and i < len(text):
        symb = reg_expr[r]
        
        if symb == 'd':
            if not text[i].isdigit():
                return False
            while i < len(text) and text[i].isdigit():
                i += 1
            r += 1
        
        elif symb == 'w':
            if not text[i].isalpha():
                return False
            while i < len(text) and text[i].isalpha():
                i += 1
            r += 1
        
        elif symb == 's':
            if not (text[i].isalpha() or text[i].isdigit()):
                return False
            while i < len(text) and (text[i].isalpha() or text[i].isdigit()):
                i += 1
            r += 1
        
        else:
            if text[i] != symb:
                return False
            i += 1
            r += 1

    return i == len(text) and r == len(reg_expr)
