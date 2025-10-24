def reg_validator(reg_expr: str, text: str) -> bool:
    if not reg_expr:  # проверка пустых reg_expr и text
        if not text:
            return True
        else:
            return False

    reg = ""

    if len(text) == 1:  # проверка случая, когда данный текст состоит из одного символа
        if text.isalpha():
            reg += "w"
        elif text.isdigit():
            reg += "d"
        else:
            reg += text

    else:  # если текст не из одного символа
        for i in range(len(text)):
            if (i == len(text) - 1):  # если эл посл в строке, то записываем его значение
                if text[i].isalpha():
                    reg += "w"
                elif text[i].isdigit():
                    reg += "d"
                else:
                    reg += text[i]

            elif not (
                text[i].isalpha() or text[i].isdigit()
            ):  # если текущий символ ни буква, ни цифра, просто записываем его
                reg += text[i]

            elif text[i].isalpha() and not text[i + 1].isalpha():
                reg += "w"

            elif text[i].isdigit() and not text[i + 1].isdigit():
                reg += "d"

    regs = [reg]

    for reg in regs:  # замена двух рядом стоящих dw, wd, ws, sw и тд на s (поиск потенц рег выр)
        for i in range(len(reg) - 1):
            duo = reg[i] + reg[i + 1]
            if ("d" in duo and "w" in duo) or ("s" in duo and ("d" in duo or "w" in duo)):
                if (i + 2) <= (len(reg) - 1):
                    newreg = reg[:i] + "s" + reg[i + 2 :]
                else:
                    newreg = reg[:i] + "s"

                if newreg not in regs:
                    regs.append(newreg)

    resultregs = regs[::]

    for i in range(len(reg_expr)):  # посимвольное сравн рег выр с каждым из списка потенц рег выр
        for reg in regs:
            if len(reg) == len(reg_expr):
                if (reg[i] == reg_expr[i]) or (
                    reg_expr[i] == "s" and (reg[i] == "d" or reg[i] == "w")
                ):
                    pass
                else:
                    if reg in resultregs:
                        resultregs.remove(reg)

            else:
                if reg in resultregs:
                    resultregs.remove(reg)

    return bool(resultregs)