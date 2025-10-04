def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
   for bit in range(left_bit, right_bit + 1):
        num ^= 1 << (bit - 1)
   return num