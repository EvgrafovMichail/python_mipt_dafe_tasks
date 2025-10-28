def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    remainders = set()
    remainders.add(0)
    if len(nums) != 0:
        last_remainder, pref_remainder = nums[0] % k, nums[0] % k

    for x in nums[1:]:
        pref_remainder = (pref_remainder + x % k) % k
        if pref_remainder in remainders:
            return True
        remainders.add(last_remainder)
        last_remainder = pref_remainder
    return False
