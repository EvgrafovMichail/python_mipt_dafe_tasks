def get_gcd(num1: int, num2: int) -> int:
    while(True):
        n1=max(num1,num2)
        n2=min(num1,num2)
        temp=n2
        n2=n1%n2
        n1=temp
        if(n2==0):
            break

    return n1
