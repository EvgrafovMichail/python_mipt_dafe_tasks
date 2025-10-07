def get_nth_digit(num: int) -> int:
    # ваш код
    k = 1
    while True:
        first = 10**(k-1) if k>1 else 0
        count = (10**k - first) // 2
        total = count * k
        if num > total:
            num -= total
            k += 1
            continue
        num1 = first + ((num - 1) // k) * 2
        pos = k - 1 - (num - 1) % k
        while pos:
            num1 //= 10
            pos -= 1
        return num1 % 10