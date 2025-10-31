def get_len_of_longest_substring(text: str) -> int:
    if len(text) == 0:
        return 0
    if len(text) == 1:
        return 1
    dic = {text[0]: 0}
    a = 0
    length = 0
    for b in range(1, len(text)):
        if text[b] in dic and dic[text[b]] >= a:
            a = dic[text[b]] + 1
        dic[text[b]] = b

        if b - a + 1 > length:
            length = b - a + 1

    return length
