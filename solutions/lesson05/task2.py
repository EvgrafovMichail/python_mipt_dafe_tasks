def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    else:
        xor_mask = 0
        arith_mask = 0
        mult_mask = 1
        for i in range(0, len(word1)):
            if ord(word1[i]) >= ord("a"):
                xor_mask ^= ord(word1[i]) + 1000
            else:
                xor_mask ^= ord(word1[i])
            if ord(word2[i]) >= ord("a"):
                xor_mask ^= ord(word2[i]) + 1000
            else:
                xor_mask ^= ord(word2[i])

            if ord(word1[i]) >= ord("a"):
                arith_mask += ord(word1[i]) + 1000
            else:
                arith_mask += ord(word1[i])
            if ord(word2[i]) >= ord("a"):
                arith_mask -= ord(word2[i]) + 1000
            else:
                arith_mask -= ord(word2[i])

            if ord(word1[i]) >= ord("a"):
                mult_mask *= ord(word1[i]) + 1000
            else:
                mult_mask *= ord(word1[i])
            if ord(word2[i]) >= ord("a"):
                mult_mask /= ord(word2[i]) + 1000
            else:
                mult_mask /= ord(word2[i])
    return 0 == arith_mask and 0 == xor_mask and (mult_mask - 1 < 1e-6)
