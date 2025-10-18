def is_palindrome(num: int) -> bool:
    reversed_num = 0
    start_num = num

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10

    return start_num == reversed_num
