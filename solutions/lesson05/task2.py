def are_anagrams(word1: str, word2: str) -> bool:
    n = len(word1)
    m = len(word2)
    if n != m:
        return False
    for i in range(n):
        if (word1[i] not in word2) or (word1.count(word1[i]) != word2.count(word2[i])):
            return False
    else:
        return True
