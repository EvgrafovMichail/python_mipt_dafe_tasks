def get_len_of_longest_substring(text: str) -> int:
    max_len = 0
    same = dict()
    max_l = list()

    if not text:
        return 0

    for i in range(0, len(text)):
        counter = i
        while counter < len(text) and text[counter] not in same:
            same.update({text[counter]: "T"})
            counter += 1
            max_len += 1

        max_l.append(max_len)
        same.clear()
        max_len = 0

    return max(max_l)
