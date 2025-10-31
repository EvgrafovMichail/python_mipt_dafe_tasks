def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    english_letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in english_letters:
        if word1.count(i) != word2.count(i):
            return False
    return True


