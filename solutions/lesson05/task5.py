def reg_validator(reg_expr: str, text: str) -> bool:  
    num=0
    text=text.lower()
    if len(reg_expr)>len(text):
        return False
    for i in range(len(reg_expr)):
        if reg_expr[i]=="d":
            if not(text[num] in "0123456789"):
                return False
            else:
                while num < len(text) and text[num] in "0123456789":
                    num+=1
        elif reg_expr[i]=="w":
            if not(text[num] in "qwertyuiopasdfghjklzxcvbnm"):
                return False
            else:
                while num < len(text) and text[num] in "qwertyuiopasdfghjklzxcvbnm":
                    num+=1
        elif reg_expr[i]=="s":
            if not(text[num] in "0123456789qwertyuiopasdfghjklzxcvbnm"):
                return False
            else:
                while num < len(text) and text[num] in "0123456789qwertyuiopasdfghjklzxcvbnm":
                    num+=1
        else:
            if num >= len(text) or text[num]!=reg_expr[i]:
                return False
            num+=1
    return num == len(text)
