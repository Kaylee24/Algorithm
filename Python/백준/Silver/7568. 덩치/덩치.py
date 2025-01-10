N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

for size in data:
    turn = 1
    for comp in data:
        if size[0] < comp[0] and size[1] < comp[1]:
            turn += 1
    print(turn, end=' ')
