def reg_validator(reg_expr: str, text: str) -> bool:
    # ваш код
    import string

    d1 = string.digits
    w1 = string.ascii_lowercase + string.ascii_uppercase
    s1 = string.ascii_lowercase + string.ascii_uppercase + string.digits

    j = 0
    new_reg_expr = ""
    for i in reg_expr:
        match i:
            case "d":
                k = j
                while j < len(text) and text[j] in d1:
                    j += 1
                if k != j:
                    new_reg_expr += "d"
            case "w":
                k = j
                while j < len(text) and text[j] in w1:
                    j += 1
                if k != j:
                    new_reg_expr += "w"
            case "s":
                k = j
                while j < len(text) and text[j] in s1:
                    j += 1
                if k != j:
                    new_reg_expr += "s"

            case _:
                while (
                    j < len(text) and text[j] not in d1 and text[j] not in w1 and text[j] not in s1
                ):
                    new_reg_expr = new_reg_expr + text[j]
                    j += 1

    if j < len(text):
        return False
    return bool(new_reg_expr == reg_expr)
