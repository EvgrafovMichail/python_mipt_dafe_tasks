def find_single_number(nums: list[int]) -> int:
    nums.sort()
    i = 0
    summa = 0
    while i + 1 <= len(nums):
        if i % 2 == 0:
            summa += nums[i]
        else:
            summa += -1 * nums[i]
        i += 1
    return summa
