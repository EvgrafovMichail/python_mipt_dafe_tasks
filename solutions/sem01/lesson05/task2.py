def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    char_count = [0] * 256

    for char in word1:
        char_count[ord(char)] += 1

    for char in word2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return all(count == 0 for count in char_count)
