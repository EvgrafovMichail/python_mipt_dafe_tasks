def int_to_roman(num: int) -> str:
    convertion_dict = {
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

    result = ""
    for arab_num in convertion_dict.keys():
        while num >= arab_num:
            result += convertion_dict[arab_num]
            num -= arab_num

    return result
