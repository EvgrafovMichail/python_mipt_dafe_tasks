def are_anagrams(word1: str, word2: str) -> bool:
    lst_1 = list(word1)
    lst_1.sort()
    lst_2 = list(word2)
    lst_2.sort()
    if lst_1 == lst_2:
        return True
    else:
        return False
