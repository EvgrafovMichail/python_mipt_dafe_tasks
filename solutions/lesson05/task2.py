def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    letters = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in letters:
        if word1.count(i) != word2.count(i):
            return False

    return True
