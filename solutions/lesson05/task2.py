def are_anagrams(word1: str, word2: str) -> bool:
    a = 0
    for i in word1:
        a += 10 ** ord(i)

    for i in word2:
        a -= 10 ** ord(i)

    if a:
        return False

    else:
        return True
