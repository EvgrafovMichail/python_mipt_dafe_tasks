def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    cnt_chars = [0] * 52

    for symb in word1:
        if symb.islower():
            cnt_chars[ord(symb) - 97] += 1
        else:
            cnt_chars[ord(symb) - 39] += 1  # -65+26

    for symb in word2:
        if symb.islower():
            cnt_chars[ord(symb) - 97] -= 1
        else:
            cnt_chars[ord(symb) - 39] -= 1  # -65+26

    for i in cnt_chars:
        if i != 0:
            return False
    return True
