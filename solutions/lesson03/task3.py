def get_nth_digit(num: int) -> int:
    length = 1
    count = 5
    while num > count * length:
        num -= count * length
        length += 1
        count = 9 * (10 ** (length - 1)) // 2
    number_index = (num - 1) // length
    digit_index = (num - 1) % length
    if length == 1:
        first_number = 0
    else:
        first_number = 10 ** (length - 1)
    number = first_number + 2 * number_index
    b = 1
    while number >= 10 ** b: b+=1
    return number % 10 ** (b - digit_index) // 10 ** (b - digit_index - 1)
