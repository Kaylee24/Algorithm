'[pypy3 : 588ms, python 3 : 시간 초과]'

N = int(input())

dp = [1]
x, y, i = 1, 1, 2
while y <= N:
    x += i
    i += 1
    y += x
    dp.append(y)

dp.pop()
cnt = [float('inf')] * (N+1)
for d in dp:
    cnt[d] = 1
for i in range(1, N):   # standard 하게는 range(1, N+1)
    for j in range(len(dp)):
        if i + dp[j] <= N:
            cnt[i+dp[j]] = min(cnt[i]+1, cnt[i+dp[j]])

print(cnt[N])