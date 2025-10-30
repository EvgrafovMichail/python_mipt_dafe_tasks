def int_to_roman(n: int) -> str:
    numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    ans = ''
    for value, key in numbers.items():
        if n > 0 and n >= key:
            ans = ans + value * (n // key)
            n %= key
        else:
            continue
    return ans