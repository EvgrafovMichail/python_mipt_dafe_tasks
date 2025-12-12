def reg_validator(reg_expr: str, text: str) -> bool:
    # ваш код
    i = 0
    for el in reg_expr:
        if i == len(text):
            return False

        if el == "s":
            if text[i].isalnum() == False:
                return False
            while i < len(text) and text[i].isalnum() == True:
                i += 1
        elif el == "d":
            if text[i].isdigit() == False:
                return False
            while i < len(text) and text[i].isdigit() == True:
                i += 1
        elif el == "w":
            if text[i].isalpha() == False:
                return False
            while i < len(text) and text[i].isalpha() == True:
                i += 1
        else:
            if text[i] != el:
                return False
            i += 1

    if i == len(text):
        return True
    return False
