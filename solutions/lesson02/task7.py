def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    # ваш код
    num_origin = str(num)

    num_reversed = num_origin[::-1]


    return num_origin == num_reversed
