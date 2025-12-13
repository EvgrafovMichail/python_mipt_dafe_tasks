def are_anagrams(word1: str, word2: str) -> bool:
    alf = [0] * 122
    if len(word1) != len(word2):
        return False
    for i in word1:
        alf[ord(i)] += 1
    for i in word2:
        alf[ord(i)] -= 1
    for i in range(len(alf)):
        if alf[i] != 0:
            return False
    return True
