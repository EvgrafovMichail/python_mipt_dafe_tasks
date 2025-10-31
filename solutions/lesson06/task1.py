def int_to_roman(num: int) -> str:
    ans = ""
    i = 0
    roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    while num:
        if num % 10:
            if num % 10 == 9:
                ans = roman[1 * 10**i] + roman[10 * 10**i] + ans
            elif num % 10 > 4:
                ans = roman[5 * 10**i] + roman[1 * 10**i] * ((num % 10) - 5) + ans
            elif num % 10 == 4:
                ans = roman[1 * 10**i] + roman[5 * 10**i] + ans
            else:
                ans = roman[1 * 10**i] * (num % 10) + ans
        i += 1
        num //= 10
    return ans
