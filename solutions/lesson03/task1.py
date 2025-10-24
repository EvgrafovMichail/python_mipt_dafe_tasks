def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
<<<<<<< HEAD
    # ваш код
    return num
=======
    mask = 0
    for i in range(left_bit, right_bit + 1):
        mask += 2 ** (i - 1)

    return num ^ mask
>>>>>>> e69d4f56c45c54e39deecc5dba6a3d657ca959f8
