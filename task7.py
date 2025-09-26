def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
      
    
    while num > 0:
        num_reversed = num % 10 + num_reversed * 10 # Умножением на 10 мы как бы переводим число спереди в следующий разряд 
        num //= 10


    return num_origin == num_reversed
