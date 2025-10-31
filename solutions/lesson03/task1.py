"""
def get_len(a):
    if a < 0:
        return 0
    elif a == 0:
        return 1
    ct = 0
    while a > 0:
        a >>= 1
        ct += 1
    return ct
"""


def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    # b = get_len(num)
    # if right_bit <= b and num != 0:
    # Насколько я понял проверка на то, чтобы правый бит не выходил за длину
    # числа в двоичном представлении не нужна, так как питон "видит" число
    # с множеством нулей перед ним, просто отбрасывает их перед выводом
    # поэтому говорить о "длине" числа бессмыслено (+ у меня некоторые тесты так
    # и не удалось пройти с сдвигами единичек в зависимости от длины)
    a = (1 << (right_bit - left_bit + 1)) - 1
    a = a << (left_bit - 1)
    num = num ^ a
    return num
