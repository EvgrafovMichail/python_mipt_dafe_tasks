def are_anagrams(word1: str, word2: str) -> bool:
    low_letters = [0] * 26
    upper_letters = [0] * 26
    a_index = ord("a")
    A_index = ord("A")

    for i in word1:
        index = ord(i)
        if index >= 97:
            low_letters[index - a_index] += 1
        elif index >= 65:
            upper_letters[index - A_index] += 1

    for j in word2:
        index = ord(j)
        if index >= 97:
            low_letters[index - a_index] -= 1
        elif index >= 65:
            upper_letters[index - A_index] -= 1

    # return not any(low_letters) and not any(upper_letters)
    for k in low_letters:
        if k:
            return False
    for p in upper_letters:
        if p:
            return False

    return True
