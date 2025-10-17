def find_single_number(nums: list[int]) -> int:
    mask = 0

    for i in range (len(nums)):

        ch = 1 << nums[i]
        mask ^= ch

    for i in range (len(bin(mask)[2:])):
        if mask ^ (1 << i) == 0:
            mask = i
    return mask

