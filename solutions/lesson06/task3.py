def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    current_sum = 0
    seen_mods = set()
    previous_mod = 0

    for num in nums:
        current_sum += num
        mod = current_sum % k
        if mod in seen_mods:
            return True
        seen_mods.add(previous_mod)
        previous_mod = mod

    return False
