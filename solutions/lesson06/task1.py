def int_to_roman(num: int) -> str:
    # ваш код

    digits_number = []
    position = 1

    while num > 0:
        digit = num % 10
        if digit != 0:
            digits_number.append(digit * position)
        num = num // 10
        position *= 10

    digits_number.reverse()

    rim_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M",
        2000: "MM",
        3000: "MMM",
    }
    rim_digit = ""
    for digit in digits_number:
        if digit in rim_dict:
            rim_digit += rim_dict[digit]
        else:
            continue

    return rim_digit
