def get_len_of_longest_substring(text: str) -> int:
    # ваш код
    max_len = 0

    for i in range(len(text)):
        uni_items = []
        act_len = 0
        for j in range(i, len(text)):
            if text[j] not in uni_items:
                uni_items.append(text[j])
                act_len += 1
            else:
                break
        if act_len > max_len:
            max_len = act_len

    return max_len
