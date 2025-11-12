def int_to_roman(num: int) -> str:
    sl = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    rc = ""
    while num != 0:
        for i in range(1000, 0, -1):
            if num >= i and i in sl:
                rc += sl[i]
                num -= i
                break
    return rc
