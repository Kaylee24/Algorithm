N = int(input())

dp = [0, 1, 2]
if N >= 3:
    dp += [0] * (N - 2)
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])