def get_len_of_longest_substring(text: str) -> int:
    if not text:
        return 0
    unic_symbols = set()
    lengths = set()
    length_sub = 0
    i = 0
    while i < len(text):
        if text[i] not in unic_symbols:
            unic_symbols.add(text[i])
            length_sub += 1
            i += 1
        else:
            lengths.add(length_sub)
            unic_symbols.remove(text[i - length_sub])
            length_sub -= 1
    lengths.add(length_sub)
    return max(lengths)


