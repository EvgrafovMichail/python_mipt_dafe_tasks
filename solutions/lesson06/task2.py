def get_len_of_longest_substring(text: str) -> int:
    last_pos = {}
    left = 0
    max_len = 0

    for right in range(len(text)):
        simvol = text[right]
        if simvol in last_pos and last_pos[simvol] >= left:
            left = last_pos[simvol] + 1
        last_pos[simvol] = right
        max_len = max(max_len, right - left + 1)

    return max_len
