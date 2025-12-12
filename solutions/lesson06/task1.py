def int_to_roman(num: int) -> str:
    dict_arabic_to_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman_num = ""
    for arabic in dict_arabic_to_roman:
        while num - arabic >= 0:
            roman_num += dict_arabic_to_roman[arabic]
            num -= arabic

    return roman_num
