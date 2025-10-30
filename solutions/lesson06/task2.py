def get_len_of_longest_substring(text: str) -> int:
    # ваш код

    res = 0
    left = 0
    unique_symbols = set()

    for right in range(len(text)):
        right_char = text[right]

        while right_char in unique_symbols:
            left_char = text[left]
            unique_symbols.remove(left_char)
            left += 1

        unique_symbols.add(right_char)
        res = max(res, right - left + 1)

    return res
