def reg_validator(reg_expr: str, text: str) -> bool:
    i = 0
    for c in reg_expr:
        if c == "d":
            if i == len(text) or not 48 <= ord(text[i]) <= 57:
                return False
            if text[i] == "0":
                i += 1
                if i < len(text) and 48 <= ord(text[i]) <= 57:
                    return False

            while i < len(text) and 48 <= ord(text[i]) <= 57:
                i += 1
        elif c == "w":
            if i == len(text) or not (65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122):
                return False
            while i < len(text) and (65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122):
                i += 1

        elif c == "s":
            if i == len(text) or not (
                48 <= ord(text[i]) <= 57 or 65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122
            ):
                return False
            while i < len(text) and (
                48 <= ord(text[i]) <= 57 or 65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122
            ):
                i += 1

        else:
            if i == len(text) or text[i] != c:
                return False
            else:
                i += 1

    if i < len(text):
        return False
    return True
