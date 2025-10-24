def reg_validator(reg_expr: str, text: str) -> bool:
    i = 0
    j = 0
    while i + 1 < len(reg_expr) and j + 1 < len(text):
        if reg_expr[i] == "d":
            while j < len(text) and text[j].isdigit():
                j += 1
            if not text[j].isdigit():
                return False
        if reg_expr[i] == "w":
            while j < len(text) and text[j].isalpha():
                j += 1
            if text[j].isalpha():
                return False
        if reg_expr[i] == "s":
            while j < len(text) and text[j].isalpha() or text[j].isdigit():
                j += 1
            if not (text[j].isalpha() or text[j].isdigit()):
                return False
        if not reg_expr[i].isalpha() and not reg_expr[i].isdigit():
            if reg_expr[i] == text[j]:
                j += 1
                i += 1
            else:
                return False
        i += 1
    return i == len(reg_expr) and j == len(text)


# print(reg_validator(input(), input()))
