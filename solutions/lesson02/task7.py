def is_palindrome(num_origin: int) -> bool:
    if num_origin < 0:
        return False
    num_reversed = 0

    len_of_num = 1
    num = num_origin
    while num // 10 > 0:
        num //= 10
        len_of_num += 1

    num = num_origin
    for i in range(1, len_of_num + 1):
        num_reversed += (num % 10) * 10 ** (len_of_num - i)
        num //= 10

    return num_origin == num_reversed
