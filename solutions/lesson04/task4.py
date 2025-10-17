def move_zeros_to_end(nums: list[int]) -> list[int]:
    c = 0
    for i in nums:
        if i == 0:
            nums.remove(0)
            c += 1
    for k in range(c):
        nums.append(0)

    return len(nums) - c
