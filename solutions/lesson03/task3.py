def get_nth_digit(num: int) -> int:
    n = num
    length = 1
    count = 5
    start = 0

    while n > length * count:
        n -= length * count
        length += 1
        start = 10 ** (length - 1)
        end = 10**length - 1
        count = ((end - start) // 2) + 1

    idx = (n - 1) // length
    number = start + idx * 2
    digit_index = (n - 1) % length
    return int(str(number)[digit_index])
