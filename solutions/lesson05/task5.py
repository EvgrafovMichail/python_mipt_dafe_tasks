def reg_validator(reg_expr: str, text: str) -> bool:  
    if text == '':
        return reg_expr == ''
    j = 0
    alph = 'qwertyuioplkjhgfdsazxcvbnm'
    numbers = '1234567890'
    for i in range(len(reg_expr)):
        
        
        if reg_expr[i] == 'd':            
            if text[j] not in numbers:
                return False
            while text[j] in numbers:
                j += 1
                if j >= len(text):
                    if i == len(reg_expr) - 1:
                        return True
                    else:
                        return False
        

        elif reg_expr[i] == 'w':
            if text[j].lower() not in alph:
                return False
            while text[j].lower() in alph:
                j += 1
                if j >= len(text):
                    if i == len(reg_expr) - 1:
                        return True
                    else:
                        return False
        
        
        elif reg_expr[i] == 's':
            if text[j].lower() not in (numbers + alph):
                return False
            while text[j].lower() in (numbers + alph):
                j += 1
                if j >= len(text):
                    if i == len(reg_expr) - 1:
                        return True
                    else:
                        return False
        
        
        else:
            if text[j] != reg_expr[i]:
                return False
            j += 1
            if j >= len(text):
                if i == len(reg_expr) - 1:
                    return True
                else:
                    return False
        

    return False