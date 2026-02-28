def get_len_of_longest_substring(text: str) -> int:
    text_len = len(text)
    max_len = 0
    symbols_count = len(set(text))

    for i in range(text_len):
        f = False

        for j in range(i + max_len, text_len):
            substring_len = j + 1 - i

            if len(set(text[i : j + 1])) == substring_len:
                max_len = substring_len
                if max_len == symbols_count:
                    f = True
                    break
            else:
                break

        if f:
            break

    return max_len
