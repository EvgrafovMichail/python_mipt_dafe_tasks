def int_to_roman(num: int) -> str:
    alf = {0: "", 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    ans = ""
    razr = 1
    n = 0
    while num != 0:
        n = num % 10
        if n == 0:
            pass
        elif n < 4:
            ans += alf[razr] * n
        elif n < 6:
            ans += alf[razr * 5] + alf[5 * razr - n * razr]
        elif n < 9:
            ans += (n - 5) * alf[razr] + alf[razr * 5]
        else:
            ans += alf[razr * 10] + alf[razr]
        num //= 10
        razr *= 10

    ans = ans[::-1]

    return ans


print(int_to_roman(1984))
