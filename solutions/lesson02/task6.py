def is_p(p):
    i = 2
    while i <= p**0.5:
        if p % i == 0:
            return 0
        i += 1
    return 1


def next_p(p):
    p_next = p
    while 1:
        p_next += 1
        if is_p(p_next) == 1:
            return p_next


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    p = 2
    n = num
    if n == 1:
        return 0
    if is_p(n) == 1:
        return n
    while p <= n**0.5:
        if n % p == 0:
            sum_of_divisors += p
            p = next_p(p)
            print(p)
        else:
            p = next_p(p)

    return sum_of_divisors
