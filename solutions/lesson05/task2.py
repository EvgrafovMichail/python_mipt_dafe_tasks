def are_anagrams(word1: str, word2: str) -> bool:
    a = list(word1)
    b = list(word2)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False