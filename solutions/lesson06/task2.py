def get_len_of_longest_substring(text: str) -> int:
    index = {}
    max_length, left = 0, 0
    for right in range(len(text)):
        if text[right] in index:
            left = max(index[text[right]] + 1, left)
        index[text[right]] = right
        max_length = max(right - left + 1, max_length)
    return max_length
