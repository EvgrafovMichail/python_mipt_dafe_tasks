def move_zeros_to_end(nums: list[int]) -> list[int]:
    n_zero = 0

    for i in nums:
        if i == 0:
            n_zero += 1

    if n_zero == 0:
        return len(nums)

    for i in range(len(nums)):
        nums.remove(0)
        nums.append(0)

    index = len(nums) - n_zero
    return index
