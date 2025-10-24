#import string
#def reg_validator(reg_expr: str, text: str) -> bool:
#    expression = []  
#    d = string.digits
#    w = string.ascii_letters
#    s = d + w
#    for ch in text:
#        if ch in d:
#            expression.append('d')
#        elif ch in w:
#            expression.append('w')
#        elif ch in s:
#            expression.append('s')
#        else:
#            expression.append(ch)
#    return set(expression) == set(reg_expr)

def reg_validator(reg_expr: str, text: str) -> bool:
    lengh_text = len(text)
    i, j = 0, 0
    char = reg_expr[j]
    while i < lengh_text and j < len(reg_expr):
        
        if char == "d":
            if not text[i].isdigit() or i >= lengh_text:
                return False
            
            while i < lengh_text and text[i].isdigit():
                i += 1
            j += 1
            
        elif char == "w":
            if not text[i].isalpha() or i >= lengh_text:
                return False
            
            while i < lengh_text and text[i].isalpha():
                i += 1
            j += 1
        
        elif char == "s":
            if not text[i].isalnum() or i >= lengh_text:
                return False
            
            while i < lengh_text and (text[i].isalnum()):
                i += 1
            j += 1
         
        else:
            if i >= len(text) or text[i] != char:
                return False
            i += 1
            j += 1    
            
            
    return i == lengh_text

#print(reg_validator(input(), input()))
