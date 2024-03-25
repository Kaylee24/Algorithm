import sys
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x: (x[0], x[1]), reverse=True)

now = meeting[0][0]
cnt = 1
for i in range(1, N):
    if meeting[i][1] <= now:
        now = meeting[i][0]
        cnt += 1

print(cnt)