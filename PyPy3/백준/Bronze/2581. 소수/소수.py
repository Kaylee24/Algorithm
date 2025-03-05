M = int(input())
N = int(input())
first, S = 0, 0
for i in range(M, N+1):
    check = 0
    if i == 1:
        check = 1
    else:
        for x in range(2, i):
            if not i%x:
                check = 1
                break
    if not check:
        if not first:
            first = i
        S += i
                
if not S:
    print(-1)
else:
    print(S)
    print(first)