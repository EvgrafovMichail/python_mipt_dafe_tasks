def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num

    temp = num
    while temp > 0:
        digit = temp % 10
        num_reversed = num_reversed * 10 + digit
        temp = temp // 10

    return num_origin == num_reversed
