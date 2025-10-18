def reg_validator(reg_expr: str, text: str) -> bool:
    index = 0
    for command in reg_expr:
        if index == len(text):
            return False
        old_index = index
        if command == "d":
            while index < len(text) and text[index].isdigit():
                index += 1
        elif command == "w":
            while index < len(text) and text[index].isalpha():
                index += 1
        elif command == "s":
            while index < len(text) and text[index].isalnum():
                index += 1
        else:
            if command == text[index]:
                index += 1
            else:
                return False
        if index == old_index:
            return False
    return index == len(text)
