def reg_validator(reg_expr: str, text: str) -> bool:
    # ваш код
    pos = 0
    text_len = len(text)

    for token in reg_expr:
        if pos >= text_len:
            return False
        ch = text[pos]

        if token == "d":
            if not ch.isdigit():
                return False
            while pos < text_len and text[pos].isdigit():
                pos += 1
        elif token == "w":
            if not ch.isalpha():
                return False
            while pos < text_len and text[pos].isalpha():
                pos += 1
        elif token == "s":
            if not (ch.isalpha() or ch.isdigit()):
                return False
            while pos < text_len and (text[pos].isalpha() or text[pos].isdigit()):
                pos += 1
        else:
            if ch != token:
                return False
            pos += 1

    return pos == text_len
