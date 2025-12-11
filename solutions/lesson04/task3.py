def find_single_number(nums: list[int]) -> int:
    a = b = 0
    for elem in nums:
        if elem >= 0:
            b ^= 1 << elem
        else:
            a ^= 1 << -elem
    k = 0
    if b:
        while b > 1:
            k += 1
            b //= 2
        return k
    elif a:
        while a > 1:
            k += 1
            a //= 2
        return -k
    else:
        return 0


if __name__ == "__main__":
    print(find_single_number([4, 1, 2, 1, 2, -1, -1, -2, -3, 0, 0, -3, 4]))
