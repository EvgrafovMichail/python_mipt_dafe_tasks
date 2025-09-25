num = int(input())

def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if num < 10:
        num_origin = num_reversed
    elif num < 0:
        num_origin != num_reversed
    else:
        while num > 0:
            num_reversed = num_reversed * 10 + num % 10
            num //= 10
    return num_origin == num_reversed
