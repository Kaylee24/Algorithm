N = int(input())

dp = [0, 1, 3, 5]
if N <= 3:
    print(dp[N])
else:
    dp += [0] * (N-3)
    for i in range(4, N+1):
        dp[i] = (dp[i-1] * 2 + (-1) ** i) % 10007
    print(dp[N])



'''
N = int(input())

dp = [0, 1, 3, 5]
if N <= 3:
    print(dp[N])
else:
    dp += [0] * (N-3)
    for i in range(4, N+1):
        if i % 2 == 0:
            dp[i] = (dp[i-1] * 2 + 1) % 10007
        else:
            dp[i] = (dp[i-1] * 2 - 1) % 10007
    print(dp[N])
'''