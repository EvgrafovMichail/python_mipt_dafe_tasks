def reg_validator(reg_expr: str, text: str) -> bool: 
    if len(reg_expr)>len(text):
        return False
    for i in range(0, len(reg_expr)):
        if reg_expr[i]=="d":
            if not text[0].isdigit():
               return False
            while text[0].isdigit():
                text = text[1:]
                if len(text)==0:
                    if len(reg_expr)-1-i !=0:
                        return False
                    return True

        elif reg_expr[i]=="w":
            if not text[0].isalpha():
               return False
            while text[0].isalpha():
                text = text[1:]
                if len(text)==0:
                    if len(reg_expr)-1-i !=0:
                        return False
                    return True

        elif reg_expr[i]=="s":
            if not ( text[0].isalpha() or text[0].isdigit()) :
               return False
            while text[0].isalpha() or text[0].isdigit():
                text = text[1:]
                if len(text)==0:
                    if len(reg_expr)-1-i !=0:
                        return False
                    return True
        else:
            if text[0] != reg_expr[i]:
                return False
            text = text[1:]
            if len(text)==0:
                    if len(reg_expr)-1-i !=0:
                        return False
                    return True
    return len(text)==0  