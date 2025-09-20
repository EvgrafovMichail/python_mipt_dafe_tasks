def get_doubled_factorial(num: int) -> int:
    if num <= 1: return 1
    if num > 1: return num * get_doubled_factorial(num - 2)
print(get_doubled_factorial(4))