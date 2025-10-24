def are_anagrams(word1: str, word2: str) -> bool:
    long = list(word1)
    for i in range(len(long)):
        if word1[i] not in word2: return False
        else: word2 = word2.replace(word1[i], "", 1)
    return True