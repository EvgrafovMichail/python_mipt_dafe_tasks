def get_nth_digit(num: int) -> int:
    n = num
    total = 5
    length = 1
    if n <= 5:
        return 2 * (n - 1)
    while n > total:
        length += 1
        total += 4.5 * 10 ** (length - 1) * length
    addition = 0
    for _ in range(length - 1):
        addition *= 10
        addition += 5
    n += addition
    index_num = (n - 1) // length
    true_num = 2 * index_num
    pos = (n - 1) % length + 1
    for _ in range(pos, length):
        true_num //= 10
    digit = true_num % 10
    return digit
