def int_to_roman(num: int) -> str:
    # составяем список из числа и создаем список для римских цифр 
    list_num = list(str(num))
    grk_letters = ["I", "V", "X", "L", "C", "D", "M", "M", "M"]

    # индекс для вывода нужных римских символов и str строка вывода
    j = 0 
    strin = ""


    # по количеству символов далее начинаем составлять итоговое выражение 
    for i in range(len(list_num)):

        letter1 = grk_letters[j]
        letter2 = grk_letters[j+1]
        letter3 = grk_letters[j+2]

        index = int(  list_num[  len(list_num)-i-1  ])

        # блок для вычисления итогового числа в римских числах
        if index < 4:     strin = letter1 * index + strin
        elif index == 4:  strin = letter1 + letter2 + strin
        elif index < 9:   strin = letter2 + (index - 5) * letter1 + strin
        elif index == 9 : strin = letter1 + letter3 + strin
        else:             strin = letter3 + strin
        j+=2

    return strin