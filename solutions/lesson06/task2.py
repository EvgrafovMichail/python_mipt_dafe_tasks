def get_len_of_longest_substring(text: str) -> int:
    result = 0
    left_pos = 0
    used_symbols = set()

    for right_pos in range(len(text)):
        while text[right_pos] in used_symbols:
            used_symbols.remove(text[left_pos])
            left_pos += 1

        used_symbols.add(text[right_pos])
        if len(used_symbols) > result:
            result = len(used_symbols)

    return result
