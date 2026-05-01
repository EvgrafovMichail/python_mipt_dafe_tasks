def reg_validator(reg_expr: str, text: str) -> bool:
    for i in reg_expr:
        if text == "":
            return False

        if i != "d" and i != "s" and i != "w":
            if text == "" or i != text[0]:
                return False
            else:
                text = text.replace(text[0], "", 1)

        elif i == "w":
            if not text[0].isalpha():
                return False
            else:
                while len(text) != 0 and text[0].isalpha():
                    text = text.replace(text[0], "", 1)

        elif i == "d":
            if not text[0].isdigit():
                return False
            else:
                while len(text) != 0 and text[0].isdigit():
                    text = text.replace(text[0], "", 1)

        elif i == "s":
            if not text[0].isalnum():
                return False
            else:
                while len(text) != 0 and text[0].isalnum():
                    text = text.replace(text[0], "", 1)

    if text != "":
        return False

    return True
