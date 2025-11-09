def reg_validator(reg_expr: str, text: str) -> bool:
    if len(reg_expr) == 0:
        return len(text) == 0

    reg_i = 0
    text_i = 0

    while reg_i < len(reg_expr) and text_i < len(text):
        current_reg = reg_expr[reg_i]

        if current_reg == "d":
            if text_i >= len(text) or not text[text_i].isdigit():
                return False

            while text_i < len(text) and text[text_i].isdigit():
                text_i += 1

        elif current_reg == "w":
            if text_i >= len(text) or not text[text_i].isalpha():
                return False

            while text_i < len(text) and text[text_i].isalpha():
                text_i += 1

        elif current_reg == "s":
            if text_i >= len(text) or not text[text_i].isalnum():
                return False

            while text_i < len(text) and text[text_i].isalnum():
                text_i += 1

        else:
            if text_i >= len(text) or text[text_i] != current_reg:
                return False
            text_i += 1

        reg_i += 1

    return reg_i == len(reg_expr) and text_i == len(text)
