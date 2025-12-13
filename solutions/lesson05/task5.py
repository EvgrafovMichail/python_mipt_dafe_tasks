def reg_validator(reg_expr, text):
    i = 0
    types = {"d": str.isdigit, "w": str.isalpha, "s": str.isalnum}

    for token in reg_expr:
        if i >= len(text):
            return False

        if token in types:
            if not types[token](text[i]):
                return False
            while i < len(text) and types[token](text[i]):
                i += 1
        else:
            if text[i] != token:
                return False
            i += 1

    return i == len(text)
