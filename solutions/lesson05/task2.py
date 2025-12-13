def are_anagrams(word1: str, word2: str) -> bool:
    if not word1 and not word2:
        return False

    sum_ord = 0
    for ch1 in word1:
        sum_ord += ord(ch1)
    for ch2 in word2:
        sum_ord -= ord(ch2)
    if not sum_ord:
        return True
    else:
        return False


# print(f"Это {are_anagrams(input("Введите анаграму "), input("Введите ёще одну "))}")
