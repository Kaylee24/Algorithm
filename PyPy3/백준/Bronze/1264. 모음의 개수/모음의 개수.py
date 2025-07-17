while True:
    S = input()
    if S == '#':
        break
        
    arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    
    for c in S:
        if c in arr:
            cnt += 1
    
    print(cnt)