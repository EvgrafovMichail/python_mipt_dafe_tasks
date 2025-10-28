def int_to_roman(num: int) -> str:
    table = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    roman_num = ""
    for roman in table:
        while num - table[roman] >= 0:
            num -= table[roman]
            roman_num += roman

    return roman_num
