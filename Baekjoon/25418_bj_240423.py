A, K = map(int, input().split())

dp = list(range(K+1))
dp[A] = 0
for i in range(A, K):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    if i*2 <= K:
        dp[i*2] = min(dp[i*2], dp[i]+1)
print(dp[K])