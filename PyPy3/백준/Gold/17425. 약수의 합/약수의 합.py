import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

f = [0] * (1000001)
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        f[j] += i

for i in range(1, 1000001):
    f[i] += f[i-1]

for num in nums:
    print(f[num])