dp = [0] * (11)
dp[1 : 4] = [1, 2, 4]
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(int(input())):
    N = int(input())
    print(dp[N])