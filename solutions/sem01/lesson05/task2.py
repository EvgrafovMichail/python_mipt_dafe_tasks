def are_anagrams(word1: str, word2: str) -> bool:
    alph1 = [0] * 52
    alph2 = [0] * 52
    for i in range(65, 91):
        alph1[i - 65] = word1.count(chr(i))
        alph2[i - 65] = word2.count(chr(i))
    for i in range(97, 123):
        alph1[i - 97] = word1.count(chr(i))
        alph2[i - 97] = word2.count(chr(i))
    if alph1 == alph2:
        return True
    return False
