def is_mirror(s):
    mirror_letters = set('AHIMOTUVWXY')
    
    for i in range(len(s)):
        if s[i] not in mirror_letters:
            return False
        
        if s[i] != s[len(s) - 1 - i]:
            return False
    
    return True

word = input().strip()

if is_mirror(word) == True:
    print("YES") 
else:
    print("NO")