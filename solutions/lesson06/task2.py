def get_len_of_longest_substring(text: str) -> int:
    last_seen = {}
    left = max_length = 0

    for right_char in enumerate(text):
        right = right_char[0]
        char = right_char[1]
        prev_pos = last_seen.get(char, -1)
        if prev_pos >= left:
            left = prev_pos + 1

        last_seen[char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length
