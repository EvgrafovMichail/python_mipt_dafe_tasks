def int_to_roman(num: int) -> str:
    romans = {0: {1: "I", 5: "V"}, 1: {1: "X", 5: "L"}, 2: {1: "C", 5: "D"}, 3: {1: "M", 5: "V_"}}
    roman = ""
    s_num = str(num)
    for i in range(len(s_num)):
        x = (num % 10 ** (i + 1)) // 10**i
        if x == 4:
            roman = romans[i][1] + romans[i][5] + roman
        elif x == 9:
            roman = romans[i][1] + romans[i + 1][1] + roman
        else:
            roman = romans[i][5] * (x // 5) + romans[i][1] * (x % 5) + roman
    return roman


print(int_to_roman(1000))
