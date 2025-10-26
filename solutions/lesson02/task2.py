def get_doubled_factorial(num: int) -> int:
    double_fact_of_num = 1
    pre_fact = 1
    pre_pre_fact = 1

    for n in range(2, num + 1):
        double_fact_of_num = n * pre_pre_fact
        pre_pre_fact = pre_fact
        pre_fact = double_fact_of_num

    return double_fact_of_num
