def reg_validator(reg_expr: str, text: str) -> bool:
    flag = True  # а вообще isdigit всякие можно было использовать?
    j = 0
    nowi = 0
    lengthtext = len(text)
    lengthreg_expr = len(reg_expr)
    curl = 0
    if (len(reg_expr) > 0) != (lengthtext > 0):
        return False
    if lengthtext < lengthreg_expr:
        return False
    for i in range(len(reg_expr)):
        curl = 0
        flag = False
        symbol = reg_expr[i]
        if symbol == "d":
            if 48 <= ord(text[nowi]) <= 57:
                nowi += 1
                flag = True
            else:
                break
            for j in range(nowi, len(text)):
                ind = ord(text[j])
                if not (48 <= ind <= 57):
                    curl += 1
                    break
            nowi = max(nowi, j)
        elif symbol == "w":
            ind = ord(text[nowi])
            if 65 <= ind <= 90 or 97 <= ind <= 122:
                nowi += 1
                flag = True
            else:
                return False
            for j in range(nowi, len(text)):
                ind = ord(text[j])
                if not (65 <= ind <= 90 or 97 <= ind <= 122):
                    nowi = j
                    curl += 1
                    break
            nowi = max(nowi, j)
        elif symbol == "s":
            ind = ord(text[nowi])
            if 65 <= ind <= 90 or 97 <= ind <= 122 or 48 <= ind <= 57:
                nowi += 1
                flag = True
            else:
                return False
            for j in range(nowi, len(text)):
                ind = ord(text[j])
                if not (65 <= ind <= 90 or 97 <= ind <= 122 or 48 <= ind <= 57):
                    nowi = j
                    curl += 1
                    break
            nowi = max(nowi, j)
        else:
            if not (text[nowi] == reg_expr[i]):
                return False
            flag = True
            if i == lengthreg_expr - 1 and nowi < lengthtext - 1:
                return False
            nowi += 1
        if not flag:
            break
    if curl:
        return False
    if nowi < lengthtext - 1:
        return False
    return flag
