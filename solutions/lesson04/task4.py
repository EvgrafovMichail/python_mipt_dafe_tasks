def move_zeros_to_end(nums: list[int]) -> list[int]:
    n = len(nums)
    head = n - 1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            j = i
            while j < head:
                nums[j] = nums[j + 1]
                j += 1
            nums[head] = 0
            head -= 1

    return head + 1