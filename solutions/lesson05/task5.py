def reg_validator(reg_expr: str, text: str) -> bool:
    index = 0
    text_len = len(text)

    for char in reg_expr:
        if index == text_len:
            return False

        if char == "d":
            num_len = 0
            while index < text_len and text[index].isdigit():
                index += 1
                num_len += 1
            if not num_len:
                return False

        elif char == "w":
            word_len = 0
            while index < text_len and text[index].isalpha():
                index += 1
                word_len += 1
            if not word_len:
                return False

        elif char == "s":
            string_len = 0
            while index < text_len and text[index].isalnum():
                index += 1
                string_len += 1
            if not string_len:
                return False

        else:
            if char != text[index]:
                return False
            index += 1
    return index == text_len
