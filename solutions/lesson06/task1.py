def int_to_roman(num: int) -> str:
    # ваш код
    val_lib = {
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
    ans = ""
    for val, symb in val_lib.items():
        while num >= val:
            ans += symb
            num -= val

    return ans
