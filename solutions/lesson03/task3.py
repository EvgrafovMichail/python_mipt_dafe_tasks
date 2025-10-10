def get_nth_digit(num: int) -> int:
    razryadnost = 1 
    col_nach_cifr = 5  
    col_cifr_raryada = col_nach_cifr * razryadnost  
    
    while col_cifr_raryada < num:
        num -= col_cifr_raryada
        razryadnost += 1
        col_nach_cifr = 5 * 9 * (10 ** (razryadnost - 2)) 
        col_cifr_raryada = col_nach_cifr * razryadnost
    
    if razryadnost == 1:
        first_number = 0
    else:
        first_number = 10 ** (razryadnost - 1)
    
    number_index = (num - 1) // razryadnost
    
    position = (num - 1) % razryadnost
    
    if razryadnost == 1:
        number = 2 * number_index
    else:
        number = first_number + 2 * number_index
    

    resalt = (number // (10 ** (razryadnost - position - 1))) % 10
    
    return resalt
#print(get_nth_digit(int(input("num = "))))