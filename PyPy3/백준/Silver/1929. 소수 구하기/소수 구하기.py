import math

M, N = map(int, input().split())
nums = [1] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if nums[i]:
        x = 2
        while i * x <= N:
            nums[i * x] = 0
            x += 1

if M == 1:
    M = 2

for i in range(M, N + 1):
    if nums[i]:
        print(i)