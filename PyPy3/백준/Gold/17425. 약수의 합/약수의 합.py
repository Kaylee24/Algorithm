import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

L = max(nums)

f = [0] * (L+1)
for i in range(1, L+1):
    for j in range(i, L+1, i):
        f[j] += i

g = [0] * (L+1)
for i in range(1, L+1):
    g[i] = g[i-1] + f[i]

for num in nums:
    print(g[num])