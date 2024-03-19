N = int(input())   # 회의의 수 N
meeting = [list(map(int, input().split())) for _ in range(N)]   # N 개의 회의 정보

cnt = 1
meeting.sort(key=lambda x : (x[0], x[1]), reverse=True)
current = meeting[0]

for i in range(1, N):
    if meeting[i][1] <= current[0]:
        current = meeting[i]
        cnt += 1

print(cnt)