def reg_validator(reg_expr: str, text: str) -> bool:
    current_pos, n = 0, len(text)

    for symbol in reg_expr:
        if symbol == "d":
            start = current_pos
            while current_pos < n and text[current_pos].isdigit():
                current_pos += 1
            if start == current_pos:
                return False
        elif symbol == "w":
            start = current_pos
            while current_pos < n and text[current_pos].isalpha():
                current_pos += 1
            if start == current_pos:
                return False
        elif symbol == "s":
            start = current_pos
            while current_pos < n and text[current_pos].isalnum():
                current_pos += 1
            if start == current_pos:
                return False
        else:
            if current_pos >= n or text[current_pos] != symbol:
                return False
            current_pos += 1

    return current_pos == n
