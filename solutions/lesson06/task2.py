def get_len_of_longest_substring(text: str) -> int:
    max = 0
    d = {}

    if len(text) == 1:
        return 1

    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[j] not in d:
                d[text[j]] = 0

            else:
                if len(d) > max:
                    max = len(d)
                d.clear()
                break

    return max
