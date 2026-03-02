t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
        
    balance = 0
    moves = 0
        
    for char in s:
        if char == '(':
            balance += 1
        else: 
            balance -= 1
            if balance < 0:
                moves += 1
                balance = 0
        
    print(moves)