def reg_validator(reg_expr: str, text: str) -> bool:
    a = 0
    b = 0
    while a < len(reg_expr) and b < len(text):
        if reg_expr[a] == "d":
            if not text[b].isdigit():
                return False
            while b < len(text) and text[b].isdigit():
                b += 1
            a += 1
        elif reg_expr[a] == "w":
            if not text[b].isalpha():
                return False
            while b < len(text) and text[a].isalpha():
                b += 1
            a += 1
        elif reg_expr[a] == "s":
            if not (text[b].isalpha() or text[b].isdigit()):
                return False
            while b < len(text) and (text[b].isalpha() or text[b].isdigit()):
                b += 1
            a += 1
        else:
            if text[b] != reg_expr[a]:
                return False
            b += 1
            a += 1
    return a == len(reg_expr) and b == len(text)
