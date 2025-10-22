def reg_validator(reg_expr: str, text: str) -> bool:
    DD = "0123456789"
    WW = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    ind_text = 0

    for i in range(len(reg_expr)):
        if ind_text >= len(text):
            return False

        if reg_expr[i] == "d":
            if text[ind_text] not in DD:
                return False
            for j in range(ind_text, len(text)):
                if text[j] not in DD:
                    break
                ind_text += 1

        elif reg_expr[i] == "w":
            if text[ind_text] not in WW:
                return False
            for j in range(ind_text, len(text)):
                if text[j] not in WW:
                    break
                ind_text += 1

        elif reg_expr[i] == "s":
            if text[ind_text] not in WW and text[ind_text] not in DD:
                return False
            for j in range(ind_text, len(text)):
                if text[j] not in WW and text[j] not in DD:
                    break
                ind_text += 1

        else:
            if text[ind_text] != reg_expr[i]:
                return False
            ind_text += 1

    if ind_text == len(text):
        return True
    else:
        return False
