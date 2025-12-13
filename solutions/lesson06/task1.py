def int_to_roman(num: int) -> str:
    s, result = 0, ""
    roman_num = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    while num > 0:
        digit = num % 10
        num //= 10
        if digit < 5:
            if digit == 4:
                result += roman_num[10**s * 5] + roman_num[10**s]
            else:
                result += roman_num[10**s] * digit
        elif digit > 5:
            if digit == 9:
                result += roman_num[10 ** (s + 1)] + roman_num[10**s]
            else:
                result += roman_num[10**s] * (digit - 5) + roman_num[10**s * 5]
        elif digit == 5:
            result += roman_num[10**s * 5]
        s += 1
    return result[::-1]


# print(int_to_roman(int(input())))
