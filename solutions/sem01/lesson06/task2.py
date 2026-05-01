def get_len_of_longest_substring(text: str) -> int:
    # ваш код
    start = 0
    seen = {}
    best = 0
    for i, ch in enumerate(text):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        best = max(best, i - start + 1)
    return best
