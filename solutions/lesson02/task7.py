num=int(input()) # задание звучит легко, его вроде через строку просто решить можно, но до этого алгоритма я часа 2 пытался додуматься
def is_palindrome(num: int) -> bool:
    num_reversed=0
    num_origin=num
    if num<10:
        num_origin=num_reversed
    elif num<0:
        num_origin!=num_reversed
    else: 
        while num>0: 
            num_reversed=num_reversed*10+num%10 # по факту алгоритм просто берет последнее цифру числа сдвигает до этого собранные числа влево и опять берет последнее число, отбрасывая ушедшее
            num//=10 
    return num_origin==num_reversed
print(is_palindrome(num))