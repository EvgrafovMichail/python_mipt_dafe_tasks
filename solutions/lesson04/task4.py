def move_zeros_to_end(nums: list[int]) -> list[int]:
    k = len(nums) - nums.count(0)

    for i in range(0, len(nums)):
        if i >= k:
            return k

        while nums[i] == 0:
            nums.pop(i)
            nums.append(0)

    return k
