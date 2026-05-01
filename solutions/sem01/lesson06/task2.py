def get_len_of_longest_substring(text: str) -> int:
    chars_in_text = {}

    start = 0
    max_len_of_longest_substring = 0
    i = 0

    while start < len(text):
        char = text[i]

        if char in chars_in_text:
            chars_in_text[char] += 1
        if chars_in_text.setdefault(char):
            max_len_of_longest_substring = max(len(chars_in_text), max_len_of_longest_substring)
            chars_in_text.clear()
            start += 1
            if i == len(text) - 1:
                return max_len_of_longest_substring
            i = start

        else:
            chars_in_text[char] = 1
            if i == len(text) - 1:
                return max(max_len_of_longest_substring, i - start + 1)
            i += 1
    return max_len_of_longest_substring
