def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    now_remains = 0
    processing = set()
    last_remains = 0

    for num in nums:
        now_remains = (now_remains + num) % k
        if now_remains in processing:
            return True
        processing.add(last_remains)
        last_remains = now_remains

    return False
