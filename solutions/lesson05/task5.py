def reg_validator(reg_expr: str, text: str) -> bool:
    position = 0

    for simbol in reg_expr:
        if simbol == "d":
            start = position
            while position < len(text) and text[position].isdigit():
                position += 1
            if position == start:
                return False

        elif simbol == "w":
            start = position
            while position < len(text) and text[position].isalpha():
                position += 1
            if position == start:
                return False

        elif simbol == "s":
            start = position
            while position < len(text) and text[position].isalnum():
                position += 1
            if position == start:
                return False

        else:
            if position >= len(text) or text[position] != simbol:
                return False
            position += 1

    return position == len(text)
