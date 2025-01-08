q = []
for _ in range(int(input())):
    q.append(int(input()))

M = max(q)

dp = [0, 1, 2, 4] + [0] * (M-3)
for i in range(4, M+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for x in q:
    print(dp[x])