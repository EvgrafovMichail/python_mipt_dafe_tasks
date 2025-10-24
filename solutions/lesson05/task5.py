def reg_validator(reg_expr: str, text: str) -> bool:
    if (reg_expr == "") and (text == ""):
        return True
    if (reg_expr == "") or (text == ""):
        return False

    i = 0
    j = 0
    while (i < len(reg_expr)) and (j < len(text)):
        if (reg_expr[i] == "d") and (text[j].isdigit()):
            while (j < len(text)) and (text[j].isdigit()):
                j += 1
        elif (reg_expr[i] == "w") and (text[j].isalpha()):
            while (j < len(text)) and (text[j].isalpha()):
                j += 1
        elif (reg_expr[i] == "s") and (text[j].isalpha() or text[j].isdigit()):
            while (j < len(text)) and (text[j].isalpha() or text[j].isdigit()):
                j += 1
        else:
            if reg_expr[i] != text[j]:
                return False
            j += 1
        i += 1

    if (i == len(reg_expr)) and (j == len(text)):
        return True
    else:
        return False
