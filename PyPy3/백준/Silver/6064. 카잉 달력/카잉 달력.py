for _ in range(int(input())):
    M, N, x, y = map(int, input().split())   # <M:N> 카잉 달력의 마지막 해

    if x == y:
        print(x)
        
    else:
        for i in range(0, int(N - x/M) + 1):
            if not (M * i + x - y) % N and (M * i + x - y) / N >= 0 and M * i + x <= M * N:
                print(M * i + x)
                break
        else:
            print(-1)
