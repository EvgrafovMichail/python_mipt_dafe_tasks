def reg_validator(reg_expr: str, text: str) -> bool:
    i, j = 0, 0
    text = text.lower()
    while i < len(reg_expr) and j < len(text):
        symbol = reg_expr[i]
        if symbol == "d":
            if not text[j].isdigit():
                return False
            while j < len(text) and text[j].isdigit():
                j += 1
        elif symbol == "w":
            if not text[j].isalpha():
                return False
            while j < len(text) and text[j].isalpha():
                j += 1
        elif symbol == "s":
            if not (text[j].isalpha() or text[j].isdigit()):
                return False
            while j < len(text) and (text[j].isalpha() or text[j].isdigit()):
                j += 1
        else:
            if text[j] != symbol:
                return False
            j += 1
        i += 1

    return i == len(reg_expr) and j == len(text)
