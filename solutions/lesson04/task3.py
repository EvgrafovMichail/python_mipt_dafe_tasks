def find_single_number(nums: list[int]) -> int:
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]

    return xor
