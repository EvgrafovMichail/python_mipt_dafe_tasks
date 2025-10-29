def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num

    if num < 0:
        num_reversed = -num
    else:
        n = num
        len = 1

        while n > 9:
            n = num / 10**len
            len += 1

        for i in range(1, len + 1):
            if i == 1:
                num_reversed += num % (10**i) * 10 ** (len - i)
            else:
                num_reversed += (num % (10**i)) // (10 ** (i - 1)) * 10 ** (len - i)

    return num_reversed == num_origin
