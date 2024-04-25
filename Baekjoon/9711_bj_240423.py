for t in range(1, int(input())+1):
    P, Q = map(int, input().split())

    dp = [0, 1]
    if P == 1:
        print(f'Case #{t}: {1%Q}')
    else:
        dp += [0] * (P-1)
        for i in range(2, P+1):
            dp[i] = (dp[i-1] + dp[i-2]) % Q
        print(f'Case #{t}: {dp[P]}')