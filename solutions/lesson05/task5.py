def reg_validator(reg_expr: str, text: str) -> bool:
    i = 0
    j = 0
    start = 0
    Nreg = len(reg_expr)
    Ntext = len(text)
    while i < Nreg:
        if j >= Ntext:
            return False
        if reg_expr[i] == "d":
            start = j
            while j < Ntext and text[j].isdigit():
                j += 1
        elif reg_expr[i] == "w":
            start = j
            while j < Ntext and text[j].isalpha():
                j += 1
        elif reg_expr[i] == "s":
            start = j
            while j < Ntext and text[j].isalnum():
                j += 1
        else:
            if text[j] == reg_expr[i]:
                j += 1
            else:
                return False
        if j == start:
            return False
        i += 1

    if i == Nreg and j == Ntext:
        return True

    return False


print(reg_validator("d-dw", "123-456abc"))
