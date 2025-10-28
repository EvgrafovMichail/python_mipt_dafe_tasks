def reg_validator(reg_expr: str, text: str) -> bool:
    new_reg_expr = ""
    substring_type = "None"

    for symbol in text:
        if symbol.isalpha():
            if substring_type != "w":
                new_reg_expr += "w"
                substring_type = "w"

        elif symbol.isdigit():
            if substring_type != "d":
                new_reg_expr += "d"
                substring_type = "d"

        else:
            new_reg_expr += symbol
            substring_type = ""

    index = 0

    for type in reg_expr:
        if index == len(new_reg_expr):
            return False

        if type == "s":
            last = index
            while index != len(new_reg_expr) and (
                new_reg_expr[index].isalpha() or new_reg_expr[index].isdigit()
            ):
                index += 1
            if last == index:
                return False

        else:
            if type != new_reg_expr[index]:
                return False
            index += 1

    return index == len(new_reg_expr)
