def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    # ваш код
    return step_curr

def f(num):
    a = 0
    for i in range(0, num):
        a+=1
    b = 0
    for i in range(0, num, 2):
        b += 1
    c = 0
    for i in range(1, num, 2):
        c += 1
    res = a*b*c
    return res
print(f(3))