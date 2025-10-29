def get_len_of_longest_substring(text: str) -> int:
    if not text:
        return 0

    char_set = set()
    max_length = 0
    left = 0

    for right in range(len(text)):
        while text[right] in char_set:
            char_set.remove(text[left])
            left += 1
        char_set.add(text[right])

        max_length = max(max_length, right - left + 1)

    return max_length
