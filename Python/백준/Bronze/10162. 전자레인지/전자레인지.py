T = int(input())

if T % 10:
    print(-1)
else:
    A, B, C = 0, 0, 0
    T //= 10
    C = T%6
    B = (T//6)%5
    A = (T//6)//5
    print(A, B, C)
