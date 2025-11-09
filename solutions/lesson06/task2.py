def get_len_of_longest_substring(text: str) -> int:
    answer = left = 0
    current = {}
    for r in range(len(text)):
        char = text[r]
        if char not in current:
            current[char] = r
        else:
            left = max(current[char] + 1, left)
            current[char] = r
        answer = max(answer, r - left + 1)
    return answer
