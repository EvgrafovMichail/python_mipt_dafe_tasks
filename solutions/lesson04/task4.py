def move_zeros_to_end(nums: list[int]) -> list[int]:
    a = len(nums)
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums.append(nums[i])
        # nums.remove(nums[i])

    print(nums)
    print(a)
    n = 0
    j = 0
    while j < len(nums) and n < a:
        if nums[j] == 0:
            nums.pop(j)
            a -= 1
        else:
            j += 1
            n += 1

    return a
