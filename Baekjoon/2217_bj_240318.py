import sys

N = int(sys.stdin.readline())
weight = [int(sys.stdin.readline()) for _ in range(N)]
weight.sort()

max_weight = 0
for i in range(N):
    sum_weight = weight[i] * (N - i)
    if max_weight < sum_weight:
        max_weight = sum_weight

print(max_weight)