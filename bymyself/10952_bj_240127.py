def sum(A, B):
    A, B = map(int, input().split())
    if A != 0 or B != 0:
        print(A + B)
        sum(A, B)
    elif A == 0 and B == 0:
        pass

A = 0
B = 0
sum(A, B)