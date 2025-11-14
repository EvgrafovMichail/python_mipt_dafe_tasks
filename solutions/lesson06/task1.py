def int_to_roman(num: int) -> str:
    d = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    ans = ""
    i = 1000
    while num > 0:
        v = num // i
        if v != 0:
            if v < 4:
                ans += d[i] * v
            elif v == 4:
                ans += d[i] + d[i * 5]
            elif 4 < v < 9:
                ans += d[i * 5] + d[i] * (v - 5)
            else:
                ans += d[i] + d[i * 10]
            num -= v * i
        i //= 10
    return ans


if __name__ == "__main__":
    print(int_to_roman(2))
