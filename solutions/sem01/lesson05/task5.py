def reg_validator(reg_expr: str, text: str) -> bool:
    i, j = 0, 0
    while i < len(reg_expr) and j < len(text):
        reg_literal = reg_expr[i]

        if reg_literal == "d":
            if not text[j].isdigit():
                return False
            while j < len(text) and text[j].isdigit():
                j += 1
            i += 1

        elif reg_literal == "w":
            if not text[j].isalpha():
                return False
            while j < len(text) and text[j].isalpha():
                j += 1
            i += 1

        elif reg_literal == "s":
            if not text[j].isalnum():
                return False
            while j < len(text) and text[j].isalnum():
                j += 1
            i += 1

        else:
            if j >= len(text) or text[j] != reg_literal:
                return False
            j += 1
            i += 1

    return i == len(reg_expr) and j == len(text)
