def get_nth_digit(num: int) -> int:
    kolv_cifr = 0
    digit_sum = 5
    if num <= digit_sum:
        return (num - 1) * 2
    while num > digit_sum:
        digit_sum += 45 * (10**kolv_cifr) * (kolv_cifr + 2)
        kolv_cifr += 1
    k = num - (digit_sum - 45 * (10 ** (kolv_cifr - 1)) * (kolv_cifr + 1)) - 1
    k1 = k // (kolv_cifr + 1)
    finall_humber = 10**kolv_cifr + k1 * 2
    return (finall_humber // (10 ** ((kolv_cifr) - (k % (kolv_cifr + 1))))) % 10
