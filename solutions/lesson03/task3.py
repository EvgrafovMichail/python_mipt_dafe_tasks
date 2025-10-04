def get_nth_digit(num: int) -> int:
    if num <= 5:
        return (num - 1) * 2
    left, right = 10, 100  # границы в которых наши числа будут расположены
    rank = 2  # разряд чисел
    summa = 5
    while True:  # алгос чтобы найти искомое число, а после цифру в нем
        if (right - left) * rank / 2 + summa < num:
            summa += (right - left) * rank / 2
            rank += 1
            left *= 10
            right *= 10
        else:
            ost = (num - summa) % rank
            chislo = (((left // 2) + (num - summa) // rank) - 1) * 2
            digit = (chislo // 10 ** ((rank - ost) if ost != 0 else 0)) % 10
            return int(digit)
