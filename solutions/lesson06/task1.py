def int_to_roman(num: int) -> str:
    # Не написал бы такой код если бы не затравка на не использование словарей
    pairs_of_borders = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )

    result = ""

    for pair in range(len(pairs_of_borders)):
        while num >= pairs_of_borders[pair][0]:
            result += pairs_of_borders[pair][1]
            num -= pairs_of_borders[pair][0]

    return result


# Кортеж неизменяем, а значит занимает меньше памяти, чем словарь,
# следовательно, данный код выигрывает в занимаемой памяти
