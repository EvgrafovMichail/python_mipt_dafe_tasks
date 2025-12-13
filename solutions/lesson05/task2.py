def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    else:
        word1_let = [0] * max(ord('z'), ord('Z'))
        word2_let = [0] * max(ord('z'), ord('Z'))

        for i in word1:
            word1_let[ord(i)] += 1

        for i in word2:
            word2_let[ord(i)] += 1

        if word1_let == word2_let:
            return True

    return False
