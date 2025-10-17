def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    if num // 10 == 0:
        return True
    else:
        num_reversed = 0
        num_origin = num
        for i in range(10, -1, -1):
            if num // (10**i) != 0:
                length = i + 1
                break
        for i in range(0, length):
            num_reversed += ((num % (10 ** (i + 1))) // (10**i)) * (10 ** (length - 1 - i))

        return num_origin == num_reversed
