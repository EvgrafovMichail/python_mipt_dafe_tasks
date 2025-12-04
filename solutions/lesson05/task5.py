def reg_validator(reg_expr: str, text: str) -> bool:
    i, j = 0, 0

    while i < len(reg_expr) and j < len(text):
        current_reg = reg_expr[i]

        if current_reg == "d":
            if not text[j].isdigit():
                return False
            while j < len(text) and text[j].isdigit():
                j += 1

        elif current_reg == "w":
            if not text[j].isalpha():
                return False
            while j < len(text) and text[j].isalpha():
                j += 1

        elif current_reg == "s":
            if not (text[j].isalpha() or text[j].isdigit()):
                return False
            while j < len(text) and (text[j].isalpha() or text[j].isdigit()):
                j += 1

        else:
            if text[j] != current_reg:
                return False
            j += 1
        i += 1
    return i == len(reg_expr) and j == len(text)
