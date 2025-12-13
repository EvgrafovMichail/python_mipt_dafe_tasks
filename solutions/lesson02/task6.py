def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    k = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            k += 1
            c = 0
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    c = 1
                    break
            if c == 0:
                if int(i**0.5) == i**0.5:
                    c = 1
            if c == 0:
                sum_of_divisors += i
            c = 0
            i = num // i
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    c = 1
                    break
            if c == 0:
                if int(i**0.5) == i**0.5:
                    c = 1
            if c == 0:
                sum_of_divisors += i
    if int(num**0.5) == num**0.5:
        k += 1
        i = num**0.5
        c = 0
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                c = 1
                break
        if c == 0:
            if int(i**0.5) == i:
                c = 1
        if c == 0:
            sum_of_divisors += i
    if k == 0:
        sum_of_divisors = num
    return sum_of_divisors
