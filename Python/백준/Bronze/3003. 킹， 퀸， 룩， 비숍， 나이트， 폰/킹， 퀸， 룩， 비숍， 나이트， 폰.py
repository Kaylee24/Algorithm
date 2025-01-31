chess = list(map(int, input().split()))

arr = [1, 1, 2, 2, 2, 8]
for i in range(6):
    chess[i] = arr[i] - chess[i]

print(*chess)