def are_anagrams(word1: str, word2: str) -> bool:
    # ваш код
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word2 == word1:
        return True
    return False
