def are_anagrams(word1: str, word2: str) -> bool:
    # ваш код
    if sorted(word1) == sorted(word2):
        return True

    return False
