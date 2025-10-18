def are_anagrams(word1: str, word2: str) -> bool:
    summa1 = 0
    summa2 = 0
    multiplication1 = 1
    multiplication2 = 1
    if len(word1) == len(word2):
        for i in range(len(word1)):
            litter1 = word1[i]
            litter2 = word2[i]
            summa1 += ord(litter1)
            summa2 += ord(litter2)
            multiplication1 *= ord(litter1)
            multiplication2 *= ord(litter2)
        if summa1 == summa2 and multiplication1 == multiplication2:
            return True
    return False
print(are_anagrams('Listen',  'Silent'))