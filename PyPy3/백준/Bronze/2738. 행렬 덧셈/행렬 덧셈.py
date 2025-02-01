N, M = map(int, input().split())
arrA = [list(map(int, input().split())) for _ in range(N)]
arrB = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        arrA[i][j] += arrB[i][j]
        
for i in range(N):
    print(*arrA[i])