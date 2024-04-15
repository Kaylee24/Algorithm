N = int(input())   # 우리의 크기
dp = [3, 7] + [0] * (N-2)

for i in range(2, N):
    dp[i] = dp[i-2] + 2 * dp[i-1]
    if dp[i-1] >= 9901:
        dp[i] %= 9901
        dp[i-1] %= 9901

print(dp[N-1] % 9901)