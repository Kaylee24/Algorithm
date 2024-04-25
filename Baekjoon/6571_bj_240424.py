N = 2
fibo = [1, 2]
while N <= 10 ** 100:
    N = fibo[-1] + fibo[-2]
    fibo.append(N)


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        temp = fibo[:]
        if A in temp:
            s = temp.index(A)
            if B in temp:
                e = temp.index(B)
            else:
                temp.append(B)
                temp.sort()
                e = temp.index(B) - 1
        else:
            temp.append(A)
            temp.sort()
            s = temp.index(A) + 1
            if B in temp:
                e = temp.index(B)
            else:
                temp.append(B)
                temp.sort()
                e = temp.index(B) - 1
        print(e - s + 1)