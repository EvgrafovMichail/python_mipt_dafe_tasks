def get_len_of_longest_substring(text: str) -> int:
    chars = set()
    le = 0
    max_len = 0
    for ri in range(len(text)):
        char = text[ri]
        while char in chars:
            chars.remove(text[le])
            le += 1
        chars.add(char)
        curr_len = ri - le + 1
        if curr_len > max_len:
            max_len = curr_len

    return max_len
