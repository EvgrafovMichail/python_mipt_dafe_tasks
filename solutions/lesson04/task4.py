def move_zeros_to_end(nums: list[int]) -> list[int]:
    i = 0

    not_trash = len(nums)
    while i < not_trash:
        if nums[i] == 0:
            nums.append(0)
            nums.pop(i)
            not_trash -= 1
        else:
            i += 1

    return not_trash
