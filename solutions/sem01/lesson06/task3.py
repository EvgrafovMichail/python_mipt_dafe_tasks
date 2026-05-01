def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    # ваш код
    prefs = {0: -1}
    s = 0
    for i, v in enumerate(nums):
        s = (s + v) % k
        if s in prefs:
            if i - prefs[s] >= 2:
                return True
        else:
            prefs[s] = i
    return False
