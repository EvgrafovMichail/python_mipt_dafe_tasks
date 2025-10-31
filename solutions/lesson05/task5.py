def reg_validator(reg_expr: str, text: str) -> bool:
    i = 0
    j = 0
    text_len = len(text)
    reg_len = len(reg_expr)

    while j < reg_len:
        if i > text_len:
            return False

        match reg_expr[j]:
            case "d":
                if i >= text_len or not text[i].isdigit():
                    return False
                while i < text_len and text[i].isdigit():
                    i += 1
                j += 1

            case "w":
                if i >= text_len or not text[i].isalpha():
                    return False
                while i < text_len and text[i].isalpha():
                    i += 1
                j += 1

            case "s":
                if i >= text_len or not text[i].isalnum():
                    return False
                while i < text_len and text[i].isalnum():
                    i += 1
                j += 1

            case _:
                if i >= text_len or text[i] != reg_expr[j]:
                    return False
                i += 1
                j += 1

    return i == text_len
