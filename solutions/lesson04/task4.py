def move_zeros_to_end(nums: list[int]) -> list[int]:
    n = 0
    while nums.count(0) != 0:
        nums.remove(0)
        n += 1
    m = len(nums)
    while n != 0:
        n -= 1
        nums.append(0)
    return m
