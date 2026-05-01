def reg_validator(reg_expr: str, text: str) -> bool:
    d = set("0123456789")
    w = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s = d | w

    groups = {"d": d, "w": w, "s": s}

    i = 0
    n = len(text)

    for token in reg_expr:
        if i >= n:
            return False

        if token in groups:
            chars = groups[token]
            if text[i] not in chars:
                return False
            while i < n and text[i] in chars:
                i += 1
        else:
            if text[i] != token:
                return False
            i += 1

    return i == n
