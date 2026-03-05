# def get_nucleotides_positions(dna):
#     if len(dna) == 0:
#         return 0

#     a_dna = []
#     b_dna = []
#     c_dna = []
#     d_dna = []

#     for i in range(len(dna)):
#         if dna[i] == 'A':
#             a_dna.append(i)

#         if dna[i] == 'B':
#             b_dna.append(i)

#         if dna[i] == 'C':
#             c_dna.append(i)

#         if dna[i] == 'D':
#             d_dna.append(i)

#     tpl = {'A': a_dna, 'B': b_dna, 'C': c_dna, 'D': d_dna}
#     return tpl


# dna = input()
# print(get_nucleotides_positions(dna))

num1 = 0.1 + 0.2
num2 = 0.3


def is_close(num1, num2):
    f = 1e8
    return num2-f < num1 < num2+f


print(is_close(num1, num2))
