def get_len_of_longest_substring(text: str) -> int:
    if len(text) == 0:
        return 0

    biggest_res = 0

    for i in range(len(text)):
        chars_set = str()
        current_len = 0

        for j in range(i, len(text)):
            if text[j] not in chars_set:
                chars_set += text[j]
                current_len += 1
            else:
                break

        biggest_res = max(biggest_res, current_len)

    return biggest_res
