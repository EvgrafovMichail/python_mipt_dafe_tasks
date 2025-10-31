def reg_validator(reg_expr: str, text: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet += alphabet.upper()
    numbers = "0123456789"
    # берем кодировщик, первый символ и сравниваем со строкой, пропускаем подобные элементы

    code = list(reg_expr)
    txt = list(text)

    index = 0
    while index < len(code):
        i1, i2, i3 = 0, 0, 0

        # блок проверок
        match code[index]:
            # проверяем соответствует ли символ тому, о чем попросили.
            # Если да, то удаляем, иначе останавливаем проверку и переходим к след символу
            case "d":
                while True:
                    if len(txt) > 0:
                        if txt[0] in numbers:
                            i1 += 1
                            txt.pop(0)
                        else:
                            break
                    else:
                        break
                # проверяем, есть ли хоть один подходящий символ
                if i1 == 0:
                    return False
                index += 1

            case "w":
                while True:
                    if len(txt) > 0:
                        if txt[0] in alphabet:
                            i2 += 1
                            txt.pop(0)
                        else:
                            break
                    else:
                        break
                if i2 == 0:
                    return False
                index += 1

            case "s":
                while True:
                    if len(txt) > 0:
                        if txt[0] in numbers or txt[0] in alphabet:
                            i3 += 1
                            txt.pop(0)
                        else:
                            break
                    else:
                        break
                if i3 == 0:
                    return False
                index += 1

            # проверяем есть ли вообще символ там и идем дальше
            case _:
                if len(txt) != 0:
                    if txt[0] != code[index]:
                        return False
                else:
                    return False
                txt.pop(0)
                index += 1

    # проверка исключений:
    # если остались еще символы
    if len(txt) != 0:
        return False

    return True
