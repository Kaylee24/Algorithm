import sys
input = sys.stdin.readline

dp = [0] * 11
dp[1:4] = [1, 2, 4]

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

result = []
pre = [[], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [2, 1], [3]]]


def f(x, k):
    global result

    if x < 4:
        if k:
            result += pre[x][k-1]
        return

    temp = 0
    for i in range(1, 4):
        temp += dp[x-i]
        if temp >= k:
            result.append(i)
            f(x-i, k-temp+dp[x-i])
            break


N, K = map(int, input().split())
if K > dp[N]:
    print(-1)
else:
    f(N, K)
    print("+".join(map(str, result)))
