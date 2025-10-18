def are_anagrams(word1: str, word2: str) -> bool:
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            return True
    return False
