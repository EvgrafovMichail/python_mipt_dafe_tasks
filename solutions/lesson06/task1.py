def int_to_roman(num: int) -> str:
    romenums = {8: "", 7: "M", 6: "D", 5: "C", 4: "L", 3: "X", 2: "V", 1: "I"}

    s = []
    i = 1
    while num > 0:
        if num % (10**i) == 9 * 10 ** (i - 1):
            s.append(romenums[2 * i + 1])
            s.append(romenums[2 * i - 1])
        elif num % (10**i) == 4 * 10 ** (i - 1):
            s.append(romenums[2 * i])
            s.append(romenums[2 * i - 1])
        else:
            n = (num // 10 ** (i - 1)) % 10
            s1 = romenums[2 * i - 1] * (n - (n // 5) * 5) + romenums[2 * i] * (n // 5)
            s.append(s1)
        num = (num // 10**i) * 10**i

        i += 1
    return "".join(s)[::-1]
