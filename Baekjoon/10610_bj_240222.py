N = list(input())
for i in range(len(N)):
    N[i] = int(N[i])

if 0 in N:
    N.pop(N.index(0))
    M = N[:]
    if sum(M) % 3 == 0:
        M.sort(reverse=True)
        for i in range(len(M)):
            M[i] = str(M[i])
        print(''.join(M) + '0')
    else:
        print(-1)
else:
    print(-1)