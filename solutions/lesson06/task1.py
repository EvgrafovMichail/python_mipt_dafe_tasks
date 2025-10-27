def int_to_roman(num: int) -> str:
    ans = ""
    num = str(num)
    letters = {
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
    for i in range(len(num)):
        digit = int(num[i]) * 10 ** (len(num) - i - 1)
        match digit:
            case 0:
                continue
            case 4 | 9 | 40 | 90 | 400 | 900:
                ans += letters[digit]
            case _ if digit < 4:
                ans += letters[1] * digit
            case _ if digit < 9:
                ans += letters[5] + letters[1] * (digit - 5)
            case _ if digit < 40:
                ans += letters[10] * (digit // 10)
            case _ if digit < 90:
                ans += letters[50] + letters[10] * (digit // 10 - 5)
            case _ if digit < 400:
                ans += letters[100] * (digit // 100)
            case _ if digit < 900:
                ans += letters[500] + letters[100] * (digit // 100 - 5)
            case _ if digit < 4000:
                ans += letters[1000] * (digit // 1000)
    return ans
