from math import sqrt, log, sin

dp = [0] * (1000001)
dp[0] = 1
for i in range(1, 1000001):
    dp[i] = (dp[int(i-sqrt(i))] + dp[int(log(i))] + dp[int(i * sin(i) ** 2)]) % 1000000

while 1:
    N = int(input())
    if N == -1:
        break
    print(dp[N])