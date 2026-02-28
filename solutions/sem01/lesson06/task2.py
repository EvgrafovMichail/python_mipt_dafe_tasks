def get_len_of_longest_substring(text: str) -> int:
    if not text:
        return 0

    result = []
    sub_str = []

    for i in range(len(text)):
        if text[i] not in sub_str:
            sub_str.append(text[i])
        else:
            result.append(sub_str)
            dupl = sub_str.index(text[i])
            sub_str = sub_str[dupl + 1 :]
            sub_str.append(text[i])

    result.append(sub_str)
    longest = max(result, key=len)
    return len(longest)
