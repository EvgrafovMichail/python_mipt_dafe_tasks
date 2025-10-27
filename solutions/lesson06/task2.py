def get_len_of_longest_substring(text: str) -> int:
    string = ""
    max_len = 0
    for i in range(1, len(text) + 1):
        for j in range(len(text) - i + 1):
            string += text[j]
            for k in range(1, i):
                if text[j + k] not in string:
                    string += text[j + k]
                else:
                    break
            if len(string) > max_len:
                max_len = len(string)
            string = ""
    return max_len
