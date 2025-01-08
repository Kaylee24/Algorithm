q = []
for _ in range(int(input())):
    q.append(int(input()))

dp = [0, 1, 2, 4]
for i in range(4, max(q)+1):
    dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)

for x in q:
    print(dp[x])