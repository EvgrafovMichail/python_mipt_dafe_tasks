def int_to_roman(num: int) -> str:
    res = ''
    razr = ['IVX', 'XLC', 'CDM', 'M--']
    for i in range(3, -1, -1):
        power = 10 ** i
        digit = num // power
        num %= power
        if digit == 0:
            continue
        s = ''
        if digit == 9:
            s += 'ix'
        elif digit >= 5:
            s += 'v' + 'i' * (digit - 5)
        elif digit == 4:
            s += 'iv'
        else:
            s += 'i' * digit
        for j in range(3):
            s = s.replace('ivx'[j], razr[i][j])
        res += s
    return res