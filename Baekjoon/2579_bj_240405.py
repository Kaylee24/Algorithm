'도움 / 아래 코드는 재귀로 풀었으나 timeout'

N = int(input())
step = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N+1)
dp[1] = step[1]
if N > 1:
    dp[2] = step[1] + step[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + step[i-1]) + step[i])

print(dp[N])



'''
def f(i, before, point):
    global max_point

    if i < 0:
        if max_point < point:
            max_point = point
        return

    # 이전 칸이 1칸 왔으면 2칸 가기
    if before == 1:
        f(i-2, 2, point+step[i])
    # 이전 칸이 2칸 왔으면 1칸, 2칸 둘 다 가보기
    if before == 2:
        f(i-1, 1, point+step[i])
        f(i-2, 2, point+step[i])


N = int(input())                                # 계단의 개수
step = [0] + [int(input()) for _ in range(N)]   # 계단에 쓰여진 점수
max_point = 0

f(N, 2, 0)
print(max_point)
'''