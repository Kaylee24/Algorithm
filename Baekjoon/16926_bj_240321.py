N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

std = M
if N <= M:
    std = N

for _ in range(R):
    for k in range(std//2):
        L, R = arr[0+k][0+k], arr[N-1-k][M-1-k]
        arr[0+k][0+k:M-1-k], arr[N-1-k][1+k:M-k] = arr[0+k][1+k:M-k], arr[N-1-k][0+k:M-1-k]
        for i in range(N-2-k, -1+k, -1):
            arr[i+1][0+k] = arr[i][0+k]
        arr[1+k][0+k] = L
        for i in range(1+k, N-1-k):
            arr[i-1][M-1-k] = arr[i][M-1-k]
        arr[N-2-k][M-1-k] = R

for i in range(N):
    print(*arr[i])