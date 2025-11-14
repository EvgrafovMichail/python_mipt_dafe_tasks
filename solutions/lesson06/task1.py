def int_to_roman(num: int) -> str:
    chars = {
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

    onroman = ""

    for lenght in range(len(str(num)), 0, -1):
        razryad = 10 ** (lenght - 1)
        consist = num // razryad
        num %= razryad
        print(consist)
        while consist:
            if consist < 4:
                onroman += chars[razryad] * consist
                break
            if consist > 5 and consist != 9:
                onroman += chars[razryad * 5] + chars[razryad] * (consist - 5)
                break
            if consist in [4, 5, 9]:
                onroman += chars[razryad * consist]
                break

    return onroman
