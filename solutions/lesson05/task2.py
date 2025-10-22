def are_anagrams(word1: str, word2: str) -> bool:
    # ваш код
    list = [0] * 128
    for i in word1:
        list[ord(i)] += ord(i)
    for g in word2:
        list[ord(g)] -= ord(g)
        if list[ord(g)] < 0:
            return False
    return True
