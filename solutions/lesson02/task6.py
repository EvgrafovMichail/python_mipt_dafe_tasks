def find_divs(numb):
    set_divs = set()
    for i in range(1, int(numb**0.5)+1):
        if numb%i==0: 
            set_divs.add(i)
            set_divs.add(numb//i)
    return sorted(set_divs)[1:]

def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    set_divs = find_divs(num)
    sum_of_divisors = sum([x for x in set_divs if len(find_divs(x))==1])
    return sum_of_divisors