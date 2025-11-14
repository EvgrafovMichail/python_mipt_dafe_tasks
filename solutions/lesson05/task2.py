def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    char_index = [0] * 128
    for i in word1:
        char_index[ord(i)] += 1
    for i in word2:
        char_index[ord(i)] -= 1
        if char_index[ord(i)] < 0:
            return False
    return True
