def int_to_roman(num: int) -> str:
    List_num = [
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

    if not 1 <= num <= 3999:
        return 0

    res_str = ""
    res_num = 0

    for numl, lit in List_num:
        while res_num + numl <= num:
            res_num += numl
            res_str += lit
            print(
                res_num,
            )
            if res_num == num:
                return res_str


print(int_to_roman(2))
