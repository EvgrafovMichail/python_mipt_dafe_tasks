def int_to_roman(num: int) -> str:
    dict = {
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
    otv = ""
    while num > 0:
        for i in dict.keys():
            if num >= i:
                num -= i
                otv += dict[i]
                break
    return otv


print(int_to_roman(27))
