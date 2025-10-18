def reg_validator(reg_expr: str, text: str) -> bool:
    j = 0
    i = 0
    while i < len(text) and j < len(reg_expr):
        char = reg_expr[j]
        match char:
            case "d":
                if not text[i].isdigit():
                    return False
                while i < len(text) and text[i].isdigit():
                    i += 1
                j += 1
            case "w":
                if not text[i].isalpha():
                    return False
                while i < len(text) and text[i].isalpha():
                    i += 1
                j += 1
            case "s":
                if not text[i].isalnum():
                    return False
                while i < len(text) and text[i].isalnum():
                    i += 1
                j += 1
            case _:
                if text[i] != char:
                    return False
                i += 1
                j += 1
    return i == len(text) and j == len(reg_expr)
