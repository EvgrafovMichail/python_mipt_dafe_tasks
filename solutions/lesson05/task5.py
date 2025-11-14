def reg_validator(reg_expr: str, text: str) -> bool:
    i = 0
    j = 0
    while j < len(text) and i < len(reg_expr):
        if reg_expr[i] == "d":
            if not text[j].isdigit():
                return False
            while j < len(text) and text[j].isdigit():
                j += 1
        if reg_expr[i] == "w":
            if not text[j].isalpha():
                return False
            while j < len(text) and text[j].isalpha():
                j += 1
        if reg_expr[i] == "s":
            if not (text[j].isalpha() or text[j].isdigit()):
                return False
            while j < len(text) and (text[j].isalpha() or text[j].isdigit()):
                j += 1
        if not reg_expr[i].isalpha():
            if text[j] != reg_expr[i]:
                return False
            j += 1
        i += 1
    return j == len(text) and i == len(reg_expr)
