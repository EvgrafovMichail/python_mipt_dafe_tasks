num = int(input())
def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0 #я сначала не понимал, что с 1 делать, но у нас изначально 0 и можно просто >1 в условие поставить
    while num >1:
        if num%2 == 0:
            multiplications_amount +=1
            num = num/2
        else:
            num = num -1
            multiplications_amount +=1     
    return multiplications_amount
print(get_multiplications_amount(num))