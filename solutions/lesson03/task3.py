def get_nth_digit(num: int) -> int:
    i = 0
    c = 5
    if num <= c:
        return (num-1) * 2
    while num > c:
        c += 45*(10**i)*(i+2)
        i += 1
    k = num - (c -45*(10**(i-1))*(i+1))-1
    k1 = k // (i+1)
    otv = 10**i + k1*2
    return (otv // (10**((i)-(k%(i+1))))) % 10