def find_single_number(nums: list[int]) -> int:
    # ваш код
    if len(nums) == 1:
        return nums[0]
    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]
    return result
