def are_anagrams(word1: str, word2: str) -> bool:
    N, M, mod = len(word1), len(word2), 1713

    if N != M:
        return False

    xor_sigma = 0
    add_sigma = 0
    multi_sigma = 1

    for pointer in range(N):
        xor_sigma ^= ord(word1[pointer]) + (0 if word1[pointer].islower() else mod)
        xor_sigma ^= ord(word2[pointer]) + (0 if word2[pointer].islower() else mod)

        add_sigma += ord(word1[pointer]) + (0 if word1[pointer].islower() else mod)
        add_sigma -= ord(word2[pointer]) + (0 if word2[pointer].islower() else mod)

        multi_sigma *= ord(word1[pointer]) + (0 if word1[pointer].islower() else mod)
        multi_sigma /= ord(word2[pointer]) + (0 if word2[pointer].islower() else mod)

    return xor_sigma == 0 and add_sigma == 0 and multi_sigma - 1 < 1e-6
