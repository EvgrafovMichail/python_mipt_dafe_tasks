def get_len_of_longest_substring(text: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1

        seen.add(text[right])
        max_len = max(max_len, right - left + 1)

    return max_len
