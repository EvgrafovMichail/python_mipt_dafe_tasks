def is_palindrome(num: int) -> bool:
    num_origin = num
    if num < 0: 
        return False
    length = 0
    num_test = num
    while num_test > 0:
        num_test //= 10
        length += 1
    num_reversed = 0
    num_test = num
    for i in range(1, length + 1):
        num_reversed += num_test % 10  * 10 ** (length - i)
        num_test //= 10
    return num_origin == num_reversed