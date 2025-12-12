def int_to_roman(num: int) -> str:
    symbols = {
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

    res = ""
    counter = 0
    while num:
        n = (num % 10) * 10**counter
        if n in symbols:
            res = symbols[n] + res
        elif n > 5 * 10**counter:
            res = symbols[5 * 10**counter] + symbols[10**counter] * (n // 10**counter - 5) + res
        else:
            res = symbols[10**counter] * (n // 10**counter) + res
        num //= 10
        counter += 1

    return res
