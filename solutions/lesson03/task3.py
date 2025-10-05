def get_nth_digit(num: int) -> int:
    left = 1
    right = 5
    if (left <= num and num <= right):
        return 2 * (num - 1)
    
    left = right + 1
    right = 95
    digits = 2
    cnt = 45
    while (num > right):
        left = right + 1
        cnt *= 10
        digits += 1
        right += cnt * digits

    order = (num - left) // digits
    digit_num = (num - left) % digits

    initial = 1
    divider = 1
    for x in range(digits - 1):
        initial *= 10
    for x in range(digits - digit_num - 1):
        divider *= 10

    n = initial + order * 2
    return (n // divider) % 10