def reg_validator(reg_expr: str, text: str) -> bool:
    if text == "":
        if reg_expr == "":
            return True
        return False
    for i in reg_expr:
        temp = text
        if i == "d":
            for j in range(len(text)):
                if text[j] in "0123456789":
                    continue
                else:
                    text = text[j:]
                    if temp == text:
                        return False
                    break
            else:
                text = ""
            continue
        if i == "w":
            for j in range(len(text)):
                if text[j] in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM":
                    continue
                else:
                    text = text[j:]
                    if temp == text:
                        return False
                    break
            else:
                text = ""
            continue
        if i == "s":
            for j in range(len(text)):
                if text[j] in "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM":
                    continue
                else:
                    text = text[j:]
                    if temp == text:
                        return False
                    break
            else:
                text = ""
            continue
        else:
            if len(text) > 0:
                if text[0] == i:
                    text = text[1:]
                else:
                    return False
        if temp == text:
            return False
    if text == "":
        return True
    return False
