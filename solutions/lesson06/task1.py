def int_to_roman(num: int) -> str:
    slovar = [
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

    rimskoe_chislo = ""
    for ne_rimskoe, rimskoe in slovar:
        while num >= ne_rimskoe:
            rimskoe_chislo += rimskoe
            num -= ne_rimskoe
    return rimskoe_chislo
