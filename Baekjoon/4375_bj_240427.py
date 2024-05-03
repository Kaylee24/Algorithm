'23:51 - 00:51, 15:24 - 15:52'
'*EOFError 처리 방법'

while True:
    try:
        N = input()
        arr, L = list(N), len(N)

        if L == arr.count('1'):
            print(L)
        else:
            num = int(''.join(['1']*L))
            N = int(N)
            if N > num:
                num *= 10
                num += 1
                L += 1

            while 1:
                if num % N == 0:
                    print(L)
                    break
                else:
                    num *= 10
                    num += 1
                    L += 1

    except EOFError:
        break