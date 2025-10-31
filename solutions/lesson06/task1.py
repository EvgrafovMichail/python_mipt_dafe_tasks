def int_to_roman(num: int) -> str:
    values = [
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
    ]

    roman = ""
    for i in range(0, len(values)):
        value = values[i][0]
        symbol = values[i][1]
        roman += symbol * (num // value)
        num %= value
    return roman
