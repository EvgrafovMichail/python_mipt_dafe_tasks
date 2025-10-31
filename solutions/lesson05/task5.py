def reg_validator(reg_expr: str, text: str) -> bool:
    if not reg_expr and not text:
        return True

    text_cur = 0
    reg_cur = 0

    while reg_cur < len(reg_expr) and text_cur < len(text):
        if reg_expr[reg_cur] == "d":
            if not text[text_cur].isdigit():
                return False

            while text_cur < len(text) and text[text_cur].isdigit():
                text_cur += 1
            reg_cur += 1

        elif reg_expr[reg_cur] == "w":
            if not text[text_cur].isalpha():
                return False

            while text_cur < len(text) and text[text_cur].isalpha():
                text_cur += 1
            reg_cur += 1

        elif reg_expr[reg_cur] == "s":
            if not text[text_cur].isalnum():
                return False

            while text_cur < len(text) and text[text_cur].isalnum():
                text_cur += 1
            reg_cur += 1

        elif text[text_cur] == reg_expr[reg_cur]:
            reg_cur += 1
            text_cur += 1
        else:
            return False

        if text_cur == len(text) and reg_cur == len(reg_expr):
            return True

    return False
