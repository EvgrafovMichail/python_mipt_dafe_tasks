def get_len_of_longest_substring(text: str) -> int:
    if text == "":
        return 0

    max_len = 1
    sub_str = []

    for start_ind in range(len(text)):
        for i in range(start_ind, len(text)):
            if text[i] not in sub_str:
                sub_str.append(text[i])
            else:
                max_len = max(max_len, len(sub_str))
                sub_str = []
                break

    return max_len
