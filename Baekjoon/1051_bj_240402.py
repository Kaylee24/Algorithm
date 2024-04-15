N, M = map(int, input().split())
num = [list(input()) for _ in range(N)]

# min(N, M) 부터 1씩 크기를 줄여가면서 꼭짓점을 찾는다.
size = min(N, M) - 1
while True:
    for i in range(N-size):
        for j in range(M-size):
            if num[i][j] == num[i+size][j] == num[i][j+size] == num[i+size][j+size]:
                exit(print((size+1)**2))
    size -= 1