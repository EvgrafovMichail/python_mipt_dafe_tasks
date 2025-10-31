def get_nth_digit(n: int) -> int:
    if n <= 5:
        return (n - 1) * 2
    n -= 5
    skolkoznach = 2
    while True:
        kolvochisel = 9 * 5 * (10 ** (skolkoznach - 2))
        vsegotcifr = kolvochisel * skolkoznach
        if n <= vsegotcifr:
            break
        n -= vsegotcifr
        skolkoznach += 1
    numchisla = (n - 1) // skolkoznach + 1
    pos = (n - 1) % skolkoznach
    firstnum = 10 ** (skolkoznach - 1)
    n = firstnum + 2 * (numchisla - 1)
    stepen10 = 10 ** (skolkoznach - pos - 1)
    res = (n // stepen10) % 10
    return res
